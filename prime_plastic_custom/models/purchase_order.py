# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from datetime import date, datetime, timedelta


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    def button_confirm(self):
        return super(
            PurchaseOrder,
            self.with_context(confirm_user_id=self.env.user.id)
        ).button_confirm()