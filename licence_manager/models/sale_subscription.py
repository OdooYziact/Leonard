from odoo import api, models, fields
import logging
_logger = logging.getLogger(__name__)


class SaleSubscription(models.Model):
    _inherit = 'sale.subscription'

    @api.onchange('stage_id')
    def onchange_check_is_licence(self):
        if self.stage_id.id == 2:
            for line_subscription in self.recurring_invoice_line_ids:
                if line_subscription.product_id.is_licence:
                    licence_id = self.env['product.licence'].create({
                        'subscription_line_id': line_subscription._origin.id,
                        'product_id': line_subscription.product_id.id,
                        'partner_id': self.partner_id.id,
                        'editor_id': line_subscription.product_id.product_tmpl_id.editor_id.id,
                        'quantity': line_subscription.quantity,
                        'provider_ids': [(6, False, line_subscription.product_id.product_tmpl_id
                                          .seller_ids.mapped('name').ids)], #a deplacer dans product licence (related)
                    })
                    line_subscription.licence_id = licence_id.id


class SaleSubscriptionLine(models.Model):
    _inherit = 'sale.subscription.line'

    licence_id = fields.Many2one(comodel_name='product.licence')


class SaleSubsriptionStage(models.Model):
    _inherit = 'sale.subscription.stage'

    status = fields.Selection([('pre_sale', 'Pre-Sale'), ('in_progress', 'In Progress'), ('canceled', 'Canceled')],
                              required=True)

    @api.depends('sale_subscription_stage')
    def change_status(self):

        if self.status == 'in_progress':

            self.in_progress = True,

        else:
            self.in_progress = False
