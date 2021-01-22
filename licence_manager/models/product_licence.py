from odoo import api, models, fields


class ProductLicence(models.Model):
    _name = "product.licence"
    _description = "Product Licence"

    subscription_line_id = fields.Many2one(string="Sub_Line_ID", comodel_name='sale.subscription.line', readonly=True)
    product_id = fields.Many2one(string="Licence", comodel_name='product.product', readonly=True)
    partner_id = fields.Many2one(string="Partner", comodel_name='res.partner', readonly=True)
    editor_id = fields.Many2one(string="Editor", comodel_name='res.partner', readonly=True)
    provider_ids = fields.Many2many(string="Provider", comodel_name='res.partner', relation='partner_licence_rel',
                                    readonly=True)
    quantity = fields.Float(string="Quantity", readonly=False)

    @api.onchange('quantity')
    def onchange_licence_qty(self):
        self.subscription_line_id.quantity = self.quantity,






#Declaration des champs utilise pour les licences. (informations a affichers dans le tableau)



#######################################################################################################################
#######PARTIE MODIFICATION DU CHAMPS QUANTITEE DANS LE TABLEAU, devra se repercuter dans les lignes d'abo !!! #########
#A faire : modif, voir pour la suppr (qui est en realite de l'archivage) et penser a l'historique
#IMPORTANT : Il faut hérité les fonction associé et venir le renseigner dans ta nouvelle table historique.