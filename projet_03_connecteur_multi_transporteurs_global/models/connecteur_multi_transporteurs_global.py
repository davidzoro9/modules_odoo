# -*- coding: utf-8 -*-
from odoo import models, fields, api

class ConnecteurMultiTransporteursGlobal(models.Model):
    _name = 'portfolio.connecteur.multi.transporteurs.global'
    _description = "Connecteur Multi-Transporteurs Global"

    def _fedex_get_shipping_label(self, picking):
        connection = self._get_fedex_connection()
        request = connection.create_label_request()
        request.add_recipient(picking.partner_id)
        request.add_packages(picking.package_ids)
        response = request.send()
        
        if response.status == 'SUCCESS':
            label_pdf = response.get_pdf_binary()
            picking.message_post(
                body="Étiquette FedEx générée avec succès.",
                attachments=[('fedex_label.pdf', label_pdf)]
            )
        else:
            raise UserError("Erreur API FedEx : %s" % response.error_message)
