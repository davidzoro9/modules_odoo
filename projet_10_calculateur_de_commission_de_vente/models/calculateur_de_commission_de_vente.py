# -*- coding: utf-8 -*-
from odoo import models, fields, api

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def _calculate_commissions(self):
        for order in self:
            if order.invoice_status == 'invoiced' and all(inv.payment_state == 'paid' for inv in order.invoice_ids):
                margin = order.margin
                salesperson = order.user_id
                commission_rate = salesperson.commission_rule_id.get_rate(margin, order.amount_total)
                
                self.env['sales.commission'].create({
                    'salesperson_id': salesperson.id,
                    'order_id': order.id,
                    'amount': order.amount_total * commission_rate,
                    'state': 'draft'
                })
