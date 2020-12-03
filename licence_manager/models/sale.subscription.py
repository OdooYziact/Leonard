from odoo import api, models
from pprint import pprint


class SaleSubscription(models.Model):
    _inherit = "sale.subscription"

    @api.model
    def create(self, values):
        if values.get('product_id', False) and ('customer_id', False):
            self.env['product.licence'].create({
                'product_id':values['product_id'],
                'customer_id':values['customer_id'],
                'quantity': values['quantity'],
            })
        res = super(SaleSubscription, self).create(values)
        print(values)
        for line in self.recurring_invoice_line_ids:
            if line.product_id == line.is_licence:  # (== self.product_id:)
                self.create.product.licence(values['product_id'], line.product_id, line.customer_id, line.quantity)
            pprint(values)
        return res
