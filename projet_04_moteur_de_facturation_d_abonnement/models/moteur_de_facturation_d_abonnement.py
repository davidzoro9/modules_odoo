# -*- coding: utf-8 -*-
from odoo import models, fields, api

class MoteurDeFacturationDAbonnement(models.Model):
    _name = 'portfolio.moteur.de.facturation.d.abonnement'
    _description = "Moteur de Facturation d'Abonnement"

    def _generate_monthly_invoices(self):
        active_subs = self.search([('state', '=', 'active'), ('next_date', '<=', fields.Date.today())])
        for sub in active_subs:
            usage_charge = self._fetch_api_usage(sub.partner_id)
            invoice_lines = []
            # Ligne de base
            invoice_lines.append((0, 0, {
                'product_id': sub.product_id.id,
                'price_unit': sub.price_unit,
            }))
            # Ligne d\'usage variable
            invoice_lines.append((0, 0, {
                'product_id': self.env.ref('saas.usage_product').id,
                'price_unit': 0.05,
                'quantity': usage_charge,
            }))
            invoice = self.env['account.move'].create({
                'move_type': 'out_invoice',
                'partner_id': sub.partner_id.id,
                'invoice_line_ids': invoice_lines
            })
            invoice.action_post()
            sub.write({'next_date': sub.next_date + relativedelta(months=1)})
