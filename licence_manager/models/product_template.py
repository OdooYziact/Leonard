from odoo import fields, models
from odoo.addons.test_impex.models import field


class ProductTemplate(models.Model):
    _inherit = "product.template"

    is_licence = fields.Boolean('Is a Licence', default=False)
    field.Boolean(string="is a licence")