from odoo import api, models, fields

import logging
_logger = logging.getLogger(__name__)


class SaleSubscription(models.Model):
    _inherit = "sale.subscription"

    @api.onchange('stage_id')
    def onchange_check_is_licence(self, option_line):
        if self.stage_id.id == 2:
            for sale_subscription in self.recurring_invoice_line_ids:
                if sale_subscription.product_id.is_licence:
                    self.env['product.licence'].create({
                        'product_id': option_line.product_id.id,

                    })
