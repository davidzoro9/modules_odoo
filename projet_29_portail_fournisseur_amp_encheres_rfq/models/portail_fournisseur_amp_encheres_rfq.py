# -*- coding: utf-8 -*-
from odoo import models, fields, api

class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    portal_bidding_enabled = fields.Boolean(string='Activer les enchères portail', default=True)
    bid_deadline = fields.Datetime(string='Date limite dépôt')

    def action_notify_vendors_for_bids(self):
        self.ensure_one()
        for line in self.partner_ids:
            # Génération d\'un token sécurisé pour le lien d\'accès sans mot de passe
            token = self.env['purchase.bid.token'].generate_token(self.id, line.id)
            # Envoi du mail d\'invitation à soumissionner
            template = self.env.ref('purchase_portal_bidding.email_template_bid_invite')
            template.with_context(token=token).send_mail(self.id, force_send=True)
