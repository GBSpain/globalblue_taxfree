# -*- coding: utf-8 -*-
from odoo import fields, models, tools, api, _
from odoo.http import request
import json
import requests


class TaxFree(models.TransientModel):
	_name = "tax.free"

	@api.model
	def TouristEligibilityDetection(self, id_country, pos_id, grossAmount):
		if not request.session['tokenTaxFree']:
			return False
		company = self.getCompanyFromPos(pos_id)
		if not company:
			return False
		if id_country:
			url_segment = "TfsIssuingService/TouristEligibilityDetection"
			country = self.env['res.country'].search([('id', '=', id_country)])
			if country:
				code = country.code
				if code:
					api_url = company.api_url + url_segment
					token = request.session['tokenTaxFree']
					myobj = {
						'alpha2Code': code,
						'GrossAmount': grossAmount,
					}
					headers = {'GB-SessionToken': token}

					x = requests.post(api_url, json=myobj, headers=headers)
					if x.text:
						json_object = json.loads(x.text)
						if 'CountryEligibility' in json_object:
							return json_object['CountryEligibility']
						if 'GrossAmountEligibility' in json_object:
							return json_object['GrossAmountEligibility']

		return False

	def getCompanyFromPos(self, pos_id):
		pos = self.env['pos.config'].search([('id', '=', pos_id)])
		if pos:
			company = pos.company_id

			return company
		return False
