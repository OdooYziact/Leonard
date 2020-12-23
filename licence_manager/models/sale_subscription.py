from odoo import api, models, fields

import logging
_logger = logging.getLogger(__name__)


class SaleSubscription(models.Model):
    _inherit = "sale.subscription"

    @api.model
    def create(self, values):
        res = super(SaleSubscription, self).create(values)
        _logger.info(values)
        for line in values['recurring_invoice_line_ids']:
            if line.product_id.is_licence:
                self.env['product.licence'].create({
                    'product_id': values['product_id'],
                    'customer_id': values['customer_id'],
                    'quantity': values['quantity'],
                })
        return res

################check_recovery_subscription_lines################

    @api.onchange('stage_id')
    def onchange_check_is_licence(self):
        if self.stage_id.id == 2:
            for line in self.recurring_invoice_line_ids:
                if line.product_id.is_licence:
                    self.env['product.licence'].create({
                        'product_id': int(product.id),
                        'customer_id': int(customer.id),
                        'quantity': float(quantity),
                    })

### Tu dois créer une ligne de product.licence en fonction de l'article de la ligne, du client de la ligne et de la quantité de la ligne.###