# -*- coding: utf-8 -*-
from odoo import models, fields, api

class HubSpotConnector(models.TransientModel):
    _name = 'hubspot.connector'
    
    def import_qualified_leads(self):
        api_url = "https://api.hubapi.com/crm/v3/objects/contacts"
        headers = {"Authorization": "Bearer %s" % self.env.company.hubspot_api_key}
        params = {"properties": "firstname,lastname,email,company,phone", "limit": 100}
        
        response = requests.get(api_url, headers=headers, params=params)
        if response.status_code == 200:
            contacts_data = response.json().get('results', [])
            for contact in contacts_data:
                props = contact.get('properties', {})
                email = props.get('email')
                if email and not self.env['res.partner'].search([('email', '=', email)]):
                    self.env['res.partner'].create({
                        'name': "%s %s" % (props.get('firstname', ''), props.get('lastname', '')),
                        'email': email,
                        'phone': props.get('phone'),
                        'company_name': props.get('company'),
                        'is_lead': True
                    })
