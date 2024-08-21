from odoo import models, fields, api

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def action_open_product_wizard(self):
        return {
            'name': 'Select Products',
            'type': 'ir.actions.act_window',
            'res_model': 'product.selection.wizard',
            'view_mode': 'form',
            'target': 'new',
            'context': {
                'default_sale_order_id': self.id,
            }
        }

class ProductSelectionWizard(models.TransientModel):
    _name = 'product.selection.wizard'
    _description = 'Wizard to Select Products'

    sale_order_id = fields.Many2one('sale.order', string='Sale Order')
    product_ids = fields.Many2many('product.product', string='Products')

    def action_add_products_to_sale_order(self):
        if self.sale_order_id:
            sale_order = self.sale_order_id
            order_lines = [(0, 0, {
                'product_id': product.id,
                'product_uom_qty': 1,
                'price_unit': product.list_price,
            }) for product in self.product_ids]
            sale_order.write({'order_line': order_lines})

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    def action_open_product_selection(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Product Selection',
            'view_mode': 'tree',
            'res_model': 'product.template',
            'domain': [],
            'context': {
                'default_sale_order_id': self.env.context.get('default_sale_order_id')
            },
            'target': 'new',
            'multi': True
        }

