# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from odoo.exceptions import UserError
from odoo.exceptions import ValidationError


class ProductModel(models.Model):
    _name = "product.model"
    _description = "Product Model"

    name = fields.Char(string="Name")