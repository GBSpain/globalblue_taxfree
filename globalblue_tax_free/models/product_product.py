# -*- coding: utf-8 -*-
import logging
from odoo import api, fields, models, tools, _

_logger = logging.getLogger(__name__)


class ProductProduct(models.Model):
	_inherit = "product.product"

	tax_amount = fields.Float(string="Tax Amount", compute="_compute_get_tax")

	def _compute_get_tax(self):
		for product in self:
			tax = product.taxes_id.amount if product.taxes_id else 0
			product.tax_amount = tax
