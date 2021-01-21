from odoo import api, models, fields

import logging
_logger = logging.getLogger(__name__)


class SaleSubscription(models.Model):
    _inherit = 'sale.subscription'

    @api.onchange('stage_id')
    def onchange_check_is_licence(self):
        if self.stage_id.id == 2:
            for line_subscription in self.recurring_invoice_line_ids:
                if line_subscription.product_id.is_licence:
                    self.env['product.licence'].create({
                        'subscription_line_id': self.line_subscription.id,
                        'product_id': line_subscription.product_id.id,
                        'partner_id': self.partner_id.id,
                        'editor_id': line_subscription.product_id.product_tmpl_id.editor_id.id,
                        'quantity': line_subscription.quantity,
                        'provider_ids': [(6, False, line_subscription.product_id.product_tmpl_id.seller_ids.mapped('name').ids)],
                    })



# Afficher plusieurs fournisseurs car si changement pendant, ca evite d'avoir un historique, in affiche jsute celui du changement
# donc on recupere pas dans la fiche produit directement mais dans la fiche abo comme ca si on change de fournisseur en meme temps ca
# conservze le fournsseur lors de l'achat de l'abo
#STATUS : actif, inactif, actif a renouveller manuellement, actif va etre renouvellé, ?
#
#
#Dupliquer le code onchange stage id 2 et le modif pour stage id 1,3,4, etc afin de supp (archiver), mettre en prépa, etc...
#Utiliser l'id de la subscription line dans le tableau mais sans l'afficher
#
