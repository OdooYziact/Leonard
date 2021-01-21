from odoo import api, models, fields

import logging
_logger = logging.getLogger(__name__)


class SaleSubscription(models.Model):
    _inherit = 'sale.subscription'

    @api.onchange('stage_id')
    def onchange_check_is_licence(self):
        if self.stage_id.id == 2:
            for sale_subscription in self.recurring_invoice_line_ids:
                if sale_subscription.product_id.is_licence:
                    self.env['product.licence'].create({
                        'product_id': sale_subscription.product_id.id,
                        'partner_id': self.partner_id.id,
                        'editor_id': sale_subscription.product_id.product_tmpl_id.editor_id.id,
                        'quantity': sale_subscription.quantity,
                        'provider_ids': sale_subscription.product_id.product_tmpl_id.seller_ids.mapped('name'),
                    })



# Afficher plusieurs fournisseurs car si changement pendant, ca evite d'avoir un historique, in affiche jsute celui du changement
# donc on recupere pas dans la fiche produit directement mais dans la fiche abo comme ca si on change de fournisseur en meme temps ca
# conservze le fournsseur lors de l'achat de l'abo