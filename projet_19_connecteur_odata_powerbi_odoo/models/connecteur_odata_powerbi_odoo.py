# -*- coding: utf-8 -*-
from odoo import models, fields, api

class ODataController(http.Controller):
    @http.route('/api/odata/v1/sale_report', type='json', auth='api_key')
    def get_sales_odata(self, **kwargs):
        # Récupération optimisée des données de vente consolidées
        records = request.env['sale.report'].search_read([], [
            'date', 'product_id', 'user_id', 'price_subtotal', 'product_uom_qty'
        ])
        return {
            'value': [{
                'Date': rec['date'],
                'ProductId': rec['product_id'][0] if rec['product_id'] else False,
                'SalespersonId': rec['user_id'][0] if rec['user_id'] else False,
                'Revenue': rec['price_subtotal'],
                'Quantity': rec['product_uom_qty']
            } for rec in records]
        }
