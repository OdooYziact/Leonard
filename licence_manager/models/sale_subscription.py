from odoo import api, models, fields

import logging
_logger = logging.getLogger(__name__)


class SaleSubscription(models.Model):
    _inherit = "sale.subscription"

    @api.onchange('stage_id')
    def onchange_check_is_licence(self):
        if self.stage_id.id == 2:
            for product_subscription in self.recurring_invoice_line_ids:
                if product_subscription.product_id.is_licence:
                    self.env['product.licence'].create({
                        'product_id': product_subscription.product_id.id,
                        'partner_id': self.partner_id.id,
                        'editor_id': product_subscription.product.editor_id.id,
                        'quantity': product_subscription.quantity,
                    })


#Creation d'abonnement comportant des licences + transfert d'informations dans mon tableau des le changement d'etat de
# l'abonnement (onchange stage_id =2)
#Observation : si dans les abonnement je decale tout dans "closed" cela ne se repercute pas dans mon tableau,
# meme si je peux tout de meme les delete manuellement.