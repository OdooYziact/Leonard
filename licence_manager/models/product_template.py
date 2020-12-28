from odoo import fields, models


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    is_licence = fields.Boolean("Is a Subscription Licence ", default=False)
    editor_id = fields.Integer("Editor ID: ")
