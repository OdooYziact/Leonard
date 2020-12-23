from odoo import api, models, fields

import logging
_logger = logging.getLogger(__name__)


class SaleSubscription(models.Model):
    _inherit = "sale.subscription"

    @api.onchange('stage_id')
    def onchange_check_is_licence(self, product, customer, quantity):
        if self.stage_id.id == 2:
            for product, customer, quantity in self.recurring_invoice_line_ids:
                if product.product_id.is_licence:
                    self.env['product.licence'].create({
                        'product_id': product.id,
                        'customer_id': customer.id,
                        'quantity': quantity,
                    })
