# -*- coding: utf-8 -*-
from odoo import models, fields, api

class DatabaseAnonymizer(models.TransientModel):
    _name = 'db.anonymizer'
    _description = 'GDPR Data Scrubbing Utility'

    def action_scrub_database(self):
        # Modification massive et directe des données sensibles pour des raisons de performance
        self.env.cr.execute("""
            UPDATE res_partner 
            SET name = 'Client Anonyme #' || id,
                email = 'client_' || id || '@test-anonyme.fr',
                phone = '0600000000',
                street = 'Rue fictive',
                city = 'Ville fictive'
            WHERE is_company = False;
        """)
        self.env.cr.execute("UPDATE res_partner_bank SET acc_number = 'FR76300060000012345678901' || id;")
        return True
