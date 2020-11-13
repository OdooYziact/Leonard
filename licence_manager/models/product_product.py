# -*- coding: utf-8 -*-

from odoo import fields, models

class ProductTemplate(models.Model):
    _inherit = 'product.template'
    is_licence = fields.Boolean(related='product_tmpl_id.is_licence')