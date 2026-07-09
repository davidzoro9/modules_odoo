# -*- coding: utf-8 -*-
from odoo import models, fields, api

class PropertyContract(models.Model):
    _name = 'property.contract'
    _description = 'Property Rental Contract'

    property_id = fields.Many2one('property.property', string='Propriété', required=True)
    tenant_id = fields.Many2one('res.partner', string='Locataire', required=True)
    rent_amount = fields.Float(string='Loyer de base')
    index_date = fields.Date(string='Date de prochaine indexation')

    def action_index_rent(self):
        for contract in self:
            # Récupération de l\'indice IRL officiel
            index_value = self.env['property.index'].get_current_index()
            contract.rent_amount = contract.rent_amount * index_value
            contract.index_date = contract.index_date + relativedelta(years=1)
