# -*- coding: utf-8 -*-
import logging
from odoo import api, fields, models, tools, _
from odoo.exceptions import RedirectWarning, UserError, ValidationError, AccessError
import base64

_logger = logging.getLogger(__name__)

class PosOrder(models.Model):
	_inherit = "pos.order"

	pdf_base64_integra = fields.Text(string="Integra PDF")
	document_identifier_integra = fields.Char(string="Integra Document ID")
	tff_void = fields.Boolean(string="TFF Void", default=False)
	totalGrossAmount = fields.Float(string="totalGrossAmount from Integra")
	message_control_refund_taxfree = fields.Text("Error messages")
	error_process_taxfree = fields.Boolean(string="Error in process TaxFree")

	def action_print_tax_free(self):
		if self.pdf_base64_integra:
			base64string = base64.b64decode(self.pdf_base64_integra)

			attachment_id = self.env['ir.attachment'].create({
				'name': _(self.pos_reference + "_ticket.pdf"),
				'type': 'binary',
				'datas': base64.encodebytes(base64string),
			})

			url = "/web/content/ir.attachment/%s/datas/?download=true" % attachment_id.id

			return {'type': 'ir.actions.act_url',
					'url': url,
					}
		else:
			raise AccessError("No hemos podido localizar el ticket.")

	def _export_for_ui(self, order):
		res = super(PosOrder, self)._export_for_ui(order)
		res["pdf_base64_integra"] = self.pdf_base64_integra
		return res

