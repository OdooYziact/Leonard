class ProductTemplate(models.Model):
    _name = "product.template"
    _inherit = ['mail.thread', 'mail.activity.mixin', 'image.mixin']
    _description = "Product Template"
    _order = "name"

    licence_ok = fields.Boolean('Is a Licence', default=False)