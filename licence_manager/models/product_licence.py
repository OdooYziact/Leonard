from odoo import fields, models


class ProductLicence(models.Model):
    _name = "product.licence"
    _description = "Product Licence"
    #_order = 'customer_id, name, editor_id, provider_id, quantity'

    product_id = fields.Many2one(string="Licence", comodel_name='product.product', readonly=True)
    customer_id = fields.Many2one(string="Customer", comodel_name='res.partner', readonly=True)
    editor_id = fields.Many2one(string="Editor", comodel_name='res.partner', readonly=True)
    provider_id = fields.Many2many(string="Provider", comodel_name='res.partner', relation='partner_licence_rel',
                                   readonly=True)
    quantity = fields.Integer(string="Quantity", readonly=False)
    an_str = fields.Char(compute="_compute_an_str")
