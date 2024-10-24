# -*- coding: utf-8 -*-
# See LICENSE file for full copyright and licensing details.

import logging
from odoo import http
from odoo.http import request
import json

_logger = logging.getLogger("POS Controller")


class Main(http.Controller):

	@http.route(['/global_blue_tax_free/TouristEligibilityDetection'], csrf=False, auth="public", type="json", method=['POST'])
	def TouristEligibilityDetection(self, **kwargs):
		response = False
		if kwargs:
			model = kwargs.get('model')
			country = kwargs.get('country')
			pos_id = kwargs.get('pos_id')
			grossAmount = kwargs.get('grossAmount')
			if model and country and pos_id:
				response = request.env[model].TouristEligibilityDetection(country, pos_id, grossAmount)
		return response

	@http.route(['/global_blue_tax_free/UserAuthenticationRequestSessionToken'], csrf=False, auth="public", type="json", method=['POST'])
	def UserAuthenticationRequestSessionToken(self, **kwargs):
		response = False
		if kwargs:
			model = kwargs.get('model')
			pos_id = kwargs.get('pos_id')
			if model and pos_id:
				response = request.env.company.UserAuthenticationRequestSessionToken(pos_id)
		return response

	@http.route(['/global_blue_tax_free/getApiMode'], csrf=False, auth="public", type="json", method=['POST'])
	def getApiMode(self, **kwargs):
		response = False
		if kwargs:
			model = kwargs.get('model')
			pos_id = kwargs.get('pos_id')
			if model and pos_id:
				response = request.env.company.getApiMode(pos_id)
		return response

	@http.route(['/global_blue_tax_free/getIssuePostUrlProd'], csrf=False, auth="public", type="json", method=['POST'])
	def getIssuePostUrlProd(self, **kwargs):
		response = False
		if kwargs:
			model = kwargs.get('model')
			pos_id = kwargs.get('pos_id')
			if model and pos_id:
				response = request.env.company.getIssuePostUrlProd(pos_id)
		return response


	@http.route(['/web/save_integra'], csrf=False, auth="public", type="http", method=['POST'])
	def save_integra(self, **post):
		if post:
			pos_reference = post.get('shopInvoiceNumber')
			if pos_reference:
				pos_order = request.env['pos.order'].sudo().search([('pos_reference', '=', pos_reference)], limit=1)
				if pos_order:
					if post.get('pdf'):
						pos_order.sudo().write({
							'pdf_base64_integra': post.get('pdf'),
							'document_identifier_integra': post.get('document_identifier'),
							'totalGrossAmount': post.get('totalGrossAmount'),
							'tff_void': False
						})
