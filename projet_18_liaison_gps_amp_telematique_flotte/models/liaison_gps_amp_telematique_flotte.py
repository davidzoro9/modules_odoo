# -*- coding: utf-8 -*-
from odoo import models, fields, api

class FleetVehicle(models.Model):
    _inherit = 'fleet.vehicle'

    geotab_device_id = fields.Char(string='ID Boîtier GPS Geotab')

    def sync_odometer_from_gps(self):
        # Appel API Geotab
        geotab_api = self.env['geotab.api.service'].connect()
        for vehicle in self.filtered('geotab_device_id'):
            gps_data = geotab_api.get_device_status(vehicle.geotab_device_id)
            if gps_data and 'odometer' in gps_data:
                self.env['fleet.vehicle.odometer'].create({
                    'vehicle_id': vehicle.id,
                    'value': gps_data['odometer'],
                    'date': fields.Date.today()
                })
