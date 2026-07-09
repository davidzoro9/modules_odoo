# -*- coding: utf-8 -*-
from odoo import models, fields, api

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    def write(self, vals):
        res = super(ProductTemplate, self).write(vals)
        # Déclenchement de la réindexation asynchrone dans Elasticsearch
        self.env['elasticsearch.sync.queue'].queue_index_job(self.ids)
        return res

    def search_in_elasticsearch(self, search_term):
        es_client = self.env['elasticsearch.client'].get_instance()
        query = {
            "query": {
                "multi_match": {
                    "query": search_term,
                    "fields": ["name^3", "description", "barcode", "default_code"]
                }
            }
        }
        response = es_client.search(index="odoo_products", body=query)
        product_ids = [hit['_id'] for hit in response['hits']['hits']]
        return self.browse(product_ids)
