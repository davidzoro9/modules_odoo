# -*- coding: utf-8 -*-
from odoo import models, fields, api

/* Code partiel d'un contrôleur de commande coffret */
class GiftBoxController(http.Controller):
    @http.route('/shop/giftbox/create', type='json', auth='public', website=True)
    def create_custom_giftbox(self, box_size_id, items_list):
        # Récupération de la commande en cours
        sale_order = request.website.sale_get_order(force_create=True)
        # Ajout de la boîte principale
        sale_order._cart_update(product_id=int(box_size_id), line_id=None, set_qty=1)
        # Ajout des composants choisis dans la boîte
        for item in items_list:
            sale_order._cart_update(
                product_id=int(item['id']),
                line_id=None,
                set_qty=int(item['qty']),
                linked_line_id=sale_order.order_line.filtered(lambda l: l.product_id.id == int(box_size_id)).id
            )
        return {'success': True}
