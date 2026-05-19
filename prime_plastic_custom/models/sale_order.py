# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from datetime import date, datetime, timedelta

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def action_confirm(self):
        return super(
            SaleOrder,
            self.with_context(confirm_user_id=self.env.user.id)
        ).action_confirm()