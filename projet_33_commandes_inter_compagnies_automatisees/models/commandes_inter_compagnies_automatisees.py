# -*- coding: utf-8 -*-
from odoo import models, fields, api

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def action_confirm(self):
        res = super(SaleOrder, self).action_confirm()
        for order in self:
            if order.partner_id.is_subsidiary:
                # Création automatique de la commande d'achat miroir
                self.env['purchase.order'].sudo().create({
                    'partner_id': order.company_id.partner_id.id, # La société vendeuse est le fournisseur
                    'company_id': order.partner_id.subsidiary_company_id.id,
                    'origin': order.name,
                    'order_line': [(0, 0, {
                        'product_id': line.product_id.id,
                        'name': line.name,
                        'product_qty': line.product_uom_qty,
                        'price_unit': line.product_id.standard_price, # Prix de transfert de base
                        'date_planned': fields.Datetime.now()
                    }) for line in order.order_line]
                })
        return res
