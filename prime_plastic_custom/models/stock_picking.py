# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from datetime import date, datetime, timedelta


class StockPickingInherit(models.Model):
    _inherit = 'stock.picking'
    _description = 'Stock Picking'

    @api.model
    def create(self, vals):
        confirm_user = self.env.context.get('confirm_user_id')
        if confirm_user:
            vals['user_id'] = confirm_user

        return super().create(vals)