from odoo import fields, models

class ProductTemplate(models.Model):
    _name = "product.template"
    licence_ok = fields.Boolean('Is a Licence', default=False)
    