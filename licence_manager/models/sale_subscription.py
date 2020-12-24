from odoo import api, models, fields

import logging
_logger = logging.getLogger(__name__)


class SaleSubscription(models.Model):
    _inherit = "sale.subscription"

    @api.onchange('stage_id')
    def onchange_check_is_licence(self):
        if self.stage_id.id == 2:
            for sale_subscription in self.recurring_invoice_line_ids:
                if sale_subscription.product_id.is_licence:
                    self.env['product.licence'].create({
                        'product_id': sale_subscription.product_id.id,
                        'customer_id': sale_subscription.company_id.id,
                        'quantity': sale_subscription.quantity,
                    })


#Dans le for, customer_id est en realite parner_id qui se voit recuperer un id via company_id.
#Creation d'abonnement comportant des licences + transfert d'informations dans mon tableau des le changement d'etat de
# l'abonnement (onchange stage_id =2)