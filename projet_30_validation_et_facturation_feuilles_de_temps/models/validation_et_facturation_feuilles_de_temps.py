# -*- coding: utf-8 -*-
from odoo import models, fields, api

class AccountAnalyticLine(models.Model):
    _inherit = 'account.analytic.line'

    state = fields.Selection([
        ('draft', 'Brouillon'),
        ('submitted', 'Soumis'),
        ('approved', 'Validé par Manager'),
        ('invoiced', 'Facturé')
    ], default='draft', string='État de validation')

    def action_submit_timesheet(self):
        self.write({'state': 'submitted'})

    def action_approve_timesheet(self):
        # Seul le manager de projet peut valider
        for line in self:
            if line.project_id.user_id != self.env.user:
                raise UserError("Seul le chef de projet peut valider ces heures.")
            line.write({'state': 'approved'})
