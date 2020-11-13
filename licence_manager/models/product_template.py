from odoo import fields, models

class ProductTemplate(models.Model):
    _name = "product.template"
    is_licence = fields.Boolean('Is a Licence', default=False)
