from odoo import fields, models


class ProductProduct(models.Model):
    _inherit = 'product.product'

    is_licence = fields.Boolean(related='product_tmpl_id.is_licence')
    editor_id = fields.Many2one(comodel_name='res.partner', related='product_tmpl_id.is_licence')
