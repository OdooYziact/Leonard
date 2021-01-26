from odoo import api, models, fields


class ProductLicence(models.Model):
    _name = "product.licence"
    _description = "Product Licence"

    subscription_line_id = fields.Many2one(string="Sub_Line_ID", comodel_name='sale.subscription.line', readonly=True)
    product_id = fields.Many2one(string="Licence", comodel_name='product.product', readonly=True)
    partner_id = fields.Many2one(string="Partner", comodel_name='res.partner', readonly=True)
    editor_id = fields.Many2one(string="Editor", comodel_name='res.partner', readonly=True)
    provider_ids = fields.Many2many(string="Provider", comodel_name='res.partner', relation='partner_licence_rel',
                                    readonly=True)
    quantity = fields.Float(string="Quantity", readonly=False)

    @api.onchange('quantity')
    def onchange_qty(self):
        for licence in self:
            licence.subscription_line_id.update({'quantity': self.quantity})
