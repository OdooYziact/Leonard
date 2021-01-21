from odoo import fields, models


class ProductLicence(models.Model):
    _name = "product.licence"
    _description = "Product Licence"

    product_id = fields.Many2one(string="Licence", comodel_name='product.product', readonly=True)
    partner_id = fields.Many2one(string="Partner", comodel_name='res.partner', readonly=True)
    editor_id = fields.Many2one(string="Editor", comodel_name='res.partner', readonly=True)
    provider_id = fields.Many2many(string="Provider", comodel_name='res.partner', relation='partner_licence_rel',
                                   readonly=True)
    quantity = fields.Integer(string="Quantity", readonly=False)




#Declaration des champs utilise pour les licences. (informations a affichers dans le tableau)



#######################################################################################################################
#######PARTIE MODIFICATION DU CAMPS QUANTITEE DANS LE TABLEAU, devra se repercuter dans les lignes d'abo !!! #########
#A faire : modif, voir pour la suppr (qui est en realite de l'archivage) et penser a l'historique
#IMPORTANT : Il faut hérité les fonction associé et venir le renseigner dans ta nouvelle table historique.