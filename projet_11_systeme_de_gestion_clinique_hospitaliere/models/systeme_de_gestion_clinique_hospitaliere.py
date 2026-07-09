# -*- coding: utf-8 -*-
from odoo import models, fields, api

class MedicalConsultation(models.Model):
    _name = 'medical.consultation'
    _description = 'Patient Medical Consultation'

    patient_id = fields.Many2one('res.partner', string='Patient', required=True, domain=[('is_patient', '=', True)])
    doctor_id = fields.Many2one('hr.employee', string='Médecin', required=True)
    symptoms = fields.Text(string='Symptômes')
    prescription_ids = fields.One2many('medical.prescription', 'consultation_id', string='Prescriptions')

    def action_complete_consultation(self):
        self.ensure_one()
        # Création de l'acte de facturation automatique
        invoice_lines = []
        for pres in self.prescription_ids:
            invoice_lines.append((0, 0, {
                'product_id': pres.medicine_id.product_variant_id.id,
                'quantity': pres.qty
            }))
        self.env['account.move'].create({
            'move_type': 'out_invoice',
            'partner_id': self.patient_id.id,
            'invoice_line_ids': invoice_lines
        })
