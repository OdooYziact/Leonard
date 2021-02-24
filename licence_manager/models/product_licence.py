from odoo import api, models, fields


class ProductLicence(models.Model):
    _name = "product.licence"
    _description = "Product Licence"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(compute='_compute_name')
    subscription_line_id = fields.Many2one(string="Sub_Line_ID", comodel_name='sale.subscription.line', readonly=True,
                                           track_visibility='onchange')
    product_id = fields.Many2one(string="Licence", comodel_name='product.product', readonly=True,
                                 track_visibility='onchange')
    partner_id = fields.Many2one(string="Partner", comodel_name='res.partner', readonly=True,
                                 track_visibility='onchange')
    editor_id = fields.Many2one(string="Editor", comodel_name='res.partner', readonly=True, track_visibility='onchange')
    provider_ids = fields.Many2many(string="Provider", comodel_name='res.partner', relation='partner_licence_rel',
                                    readonly=True, track_visibility='onchange')
    quantity = fields.Float(string="Quantity", readonly=False, track_visibility='onchange')

    @api.onchange('quantity')
    def onchange_qty(self):
        for licence in self:
            licence.subscription_line_id.update({'quantity': self.quantity})

    def _compute_name(self):
        for licence in self:
            if self.product_id:
                licence.write({'name': self.product_id.name})
