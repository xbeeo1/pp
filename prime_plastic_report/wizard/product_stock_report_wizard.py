from odoo import models, fields, api
from odoo.exceptions import ValidationError

class ProductStockReport(models.Model):
    _name = "product.stock.report"
    _description = "Product Stock Report"

    product_ids = fields.Many2many("product.product", string="Product" ,required=True)
    warehouse_id = fields.Many2one("stock.warehouse", string="Warehouse" ,required=True)
    def print_report(self):

        missing_products = []

        for product in self.product_ids:
            bom = self.env['mrp.bom'].search([
                ('product_tmpl_id', '=', product.product_tmpl_id.id)
            ], limit=1)

            if not bom:
                missing_products.append(product.display_name)

        if missing_products:
            product_list = ", ".join(missing_products)
            raise ValidationError(
                f"No Bill of Materials (BOM) exists for the following product(s): {product_list}"
            )

        return self.env.ref(
            'prime_plastic_report.action_product_stock_report'
        ).report_action(self)

    def get_report_data(self):
        result = []

        for product in self.product_ids:
            locations = self.env['stock.location'].search([
                ('warehouse_id', '=', self.warehouse_id.id)
            ])
            quants_prod = self.env['stock.quant'].search([
                ('product_id', '=', product.id),
                ('location_id', 'in', locations.ids)
            ])

            onhand_prod = sum(quants_prod.mapped('quantity'))

            product_data = {
                'product_name': product.name,
                'onhand_qty_prod': onhand_prod,
                'code_prod': product.default_code,
                'unit_prod': product.uom_id.name,
                'color_prod': product.product_color_id.name if product.product_color_id else '',
                'material_prod': product.product_material_id.name if product.product_material_id else '',
                'model_prod': product.product_model_id.name if product.product_model_id else '',
                'components': []
            }

            bom = self.env['mrp.bom'].search([
                ('product_tmpl_id', '=', product.product_tmpl_id.id)
            ], limit=1)

            if bom:
                for line in bom.bom_line_ids:
                    quants = self.env['stock.quant'].search([
                        ('product_id', '=', line.product_id.id),
                        ('location_id', 'in', locations.ids)
                    ])

                    onhand = sum(quants.mapped('quantity'))

                    product_data['components'].append({
                        'component_name': line.product_id.name,
                        'onhand_qty': onhand,
                        'code': line.product_id.default_code,
                        'unit':line.product_id.uom_id.name,
                        'color': line.product_id.product_color_id.name if line.product_id.product_color_id else '',
                        'material': line.product_id.product_material_id.name if line.product_id.product_material_id else '',
                        'model': line.product_id.product_model_id.name if line.product_id.product_model_id else '',
                    })

            result.append(product_data)

        return result


class action_product_stock_report(models.AbstractModel):
    _name = 'report.prime_plastic_report.product_stock_report_template'
    _description = 'Product Stock Report'

    def _get_report_values(self, docids, data=None):
        docs = self.env['product.stock.report'].browse(docids)
        return {
            'doc_ids': docids,
            'doc_model': 'product.stock.report',
            'docs': docs,
            'report_data': docs.get_report_data(),
        }