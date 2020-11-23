# -*- coding: utf-8 -*-

from odoo import fields, models
from odoo.addons.test_impex.models import field


class ProductProduct(models.Model):
    _inherit = 'product.product'

    is_licence = fields.Boolean(related='product_tmpl_id.is_licence')
    field.Boolean(string="is a licence")