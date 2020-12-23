from odoo import api, models, fields

import logging
_logger = logging.getLogger(__name__)


class SaleSubscription(models.Model):
    _inherit = "sale.subscription"

    @api.onchange('stage_id')
    def onchange_check_is_licence(self):
        if self.stage_id.id == 2:
            for lines in self.recurring_invoice_line_ids:
                if lines.product_id.is_licence in self.recurring_invoice_line_ids:
                    self.env['product.licence'].create({
                        'product_id': int(),
                        'customer_id': int(),
                        'quantity': float(),
                    })