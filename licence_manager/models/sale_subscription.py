from odoo import api, models, fields

import logging
_logger = logging.getLogger(__name__)


class SaleSubscription(models.Model):
    _inherit = "sale.subscription"

    @api.onchange('stage_id')
    def onchange_check_is_licence(self):
        if self.stage_id.id == 2:
            for product, customer, quantity in self.recurring_invoice_line_ids:
                if product.is_licence:
                    self.env['product.licence'].create({
                        'product_id': product,
                        'customer_id': customer,
                        'quantity': quantity,
                    })
