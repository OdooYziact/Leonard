# -*- coding: utf-8 -*-

from odoo import fields, models

class ProductTemplate(models.Model):
    _inherit = 'product.template'
    licence_ok = fields.Boolean('Is a Licence', default=False)