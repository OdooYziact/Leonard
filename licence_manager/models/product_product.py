# -*- coding: utf-8 -*-

from odoo import fields, models


class ProductProduct(models.Model):
    _inherit = 'product.product'

    is_licence = fields.Boolean(related='product_template_form_view')
