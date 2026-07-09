# -*- coding: utf-8 -*-
from odoo import models, fields, api

class StockPicking(models.Model):
    _inherit = 'stock.picking'

    def action_dispatch_to_agv(self):
        self.ensure_one()
        agv_system = self.env['iot.device'].search([('type', '=', 'agv_router')], limit=1)
        if agv_system:
            payload = {
                'picking_id': self.id,
                'locations': [{'source': line.location_id.name, 'dest': line.location_dest_id.name} for line in self.move_line_ids],
                'priority': self.priority
            }
            agv_system.send_websocket_payload(payload)
            self.write({'state': 'assigned'})
