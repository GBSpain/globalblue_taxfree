# -*- coding: utf-8 -*-
import logging
from odoo import api, fields, models, _, Command

_logger = logging.getLogger(__name__)


class PosSession(models.Model):
    _inherit = 'pos.session'


    def _get_pos_ui_product_product(self, params):
        params["search_params"]["fields"].append("tax_amount")
        return super(PosSession, self)._get_pos_ui_product_product(params)
