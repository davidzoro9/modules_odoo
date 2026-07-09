# -*- coding: utf-8 -*-
from odoo import models, fields, api

class FacturationElectroniqueZatcaKsa(models.Model):
    _name = 'portfolio.facturation.electronique.zatca.ksa'
    _description = "Facturation Électronique ZATCA KSA"

    def _generate_zatca_xml(self, invoice):
        xml_content = self._render_ubl_template(invoice)
        private_key = self.company_id.zatca_private_key
        certificate = self.company_id.zatca_certificate
        
        signed_xml = self.cryptography_sign_xml(xml_content, private_key, certificate)
        hash_value = self.calculate_xml_hash(signed_xml)
        
        invoice.write({
            'zatca_xml_file': base64.b64encode(signed_xml.encode('utf-8')),
            'zatca_hash': hash_value,
            'zatca_status': 'ready'
        })
