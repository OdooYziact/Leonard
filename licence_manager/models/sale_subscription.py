from odoo import api, models, fields

import logging
_logger = logging.getLogger(__name__)


class SaleSubscription(models.Model):
    _inherit = "sale.subscription"

    @api.onchange('stage_id')
    def onchange_check_is_licence(self, product_id, customer_id, quantity):
        if self.stage_id.id == 2:
            for sale_subscription_line in self.recurring_invoice_line_ids:
                if sale_subscription_line.product_id.is_licence:
                    self.env['product.licence'].create(
                        dict(product_id=int(product.id), customer_id=int(customer.id), quantity=float()))
