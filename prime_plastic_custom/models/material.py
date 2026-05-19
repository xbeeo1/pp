# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from odoo.exceptions import UserError
from odoo.exceptions import ValidationError


class MaterialMaterial(models.Model):
    _name = "material.material"
    _description = "Material"

    name = fields.Char(string="Name")