# -*- coding: utf-8 -*-
from odoo import models, fields, api

class HrAttendance(models.Model):
    _inherit = 'hr.attendance'

    check_in_latitude = fields.Float(string='Latitude Entrée')
    check_in_longitude = fields.Float(string='Longitude Entrée')
    is_geofenced = fields.Boolean(string='Dans la zone autorisée', compute='_check_geofencing', store=True)

    @api.depends('check_in_latitude', 'check_in_longitude', 'employee_id')
    def _check_geofencing(self):
        for attendance in self:
            # Récupération du site client associé à la mission du jour
            site = attendance.employee_id.get_current_assigned_site()
            if site and attendance.check_in_latitude:
                distance = attendance._calculate_distance(
                    attendance.check_in_latitude, attendance.check_in_longitude,
                    site.latitude, site.longitude
                )
                attendance.is_geofenced = (distance <= 100.0) # Moins de 100 mètres
            else:
                attendance.is_geofenced = True
