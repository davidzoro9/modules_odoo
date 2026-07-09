# -*- coding: utf-8 -*-
from odoo import models, fields, api

class ShopifyConnector(models.AbstractModel):
    _name = 'shopify.connector'
    _description = 'Shopify Integration Services'

    def update_shopify_inventory(self, product):
        shopify_product_id = product.shopify_id
        qty_available = product.qty_available
        
        url = "https://%s/admin/api/2023-10/inventory_levels/set.json" % self.get_shopify_domain()
        headers = {"X-Shopify-Access-Token": self.get_access_token()}
        payload = {
            "location_id": self.get_shopify_location_id(),
            "inventory_item_id": product.shopify_inventory_item_id,
            "available": int(qty_available)
        }
        response = requests.post(url, headers=headers, json=payload)
        return response.status_code == 200
