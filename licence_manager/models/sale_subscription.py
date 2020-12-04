from odoo import api, models

import logging
_logger = logging.getLogger(__name__)


class SaleSubscription(models.Model):
    _inherit = "sale.subscription"

    @api.model
    def create(self, values):
        res = super(SaleSubscription, self).create(values)
        _logger.info(values)
        for line in values['recurring_invoice_line_ids']:
            if line.product_id.is_lience:
                self.env['product.licence'].create({
                    'product_id': values['product_id'],
                    'customer_id': values['customer_id'],
                    'quantity': values['quantity'],
                })
        return res
