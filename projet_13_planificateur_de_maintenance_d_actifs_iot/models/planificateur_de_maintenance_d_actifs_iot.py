# -*- coding: utf-8 -*-
from odoo import models, fields, api

class MaintenanceEquipment(models.Model):
    _inherit = 'maintenance.equipment'

    current_cycles = fields.Integer(string='Cycles Actuels')
    cycle_threshold = fields.Integer(string='Seuil Alerte Cycles', default=10000)

    def register_iot_cycles(self, increment):
        for rec in self:
            rec.current_cycles += increment
            if rec.current_cycles >= rec.cycle_threshold:
                # Création automatique de la demande de maintenance
                self.env['maintenance.request'].create({
                    'name': 'Maintenance Préventive de Seuil pour %s' % rec.name,
                    'equipment_id': rec.id,
                    'maintenance_type': 'preventive',
                    'user_id': rec.technician_user_id.id
                })
                rec.current_cycles = 0  # Reset
