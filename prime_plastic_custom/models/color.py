# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from odoo.exceptions import UserError
from odoo.exceptions import ValidationError


class ColorColor(models.Model):
    _name = "color.color"
    _description = "Color"

    name = fields.Char(string="Name")