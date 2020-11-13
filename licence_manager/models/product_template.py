from odoo import fields, models

class ProductTemplate(models.Model):
    _inherit = "product.template"

    is_licence = fields.Boolean('Is a Licence', default=False)
