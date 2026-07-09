# -*- coding: utf-8 -*-
from odoo import models, fields, api

class QualityCheck(models.Model):
    _inherit = 'quality.check'

    inspector_signature = fields.Binary(string='Signature Inspecteur', required=True)
    conformity_checklist = fields.Boolean(string='Conformité visuelle et dimensionnelle validée')

    def action_pass_quality_control(self):
        self.ensure_one()
        if not self.conformity_checklist or not self.inspector_signature:
            raise UserError("Vous devez valider la checklist et signer le rapport de contrôle.")
        self.write({'quality_state': 'pass', 'control_date': fields.Datetime.now()})
        # Libération automatique du stock bloqué
        self.picking_id.action_release_quarantine()
