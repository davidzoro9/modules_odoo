# -*- coding: utf-8 -*-
from odoo import models, fields, api

class ProjectTask(models.Model):
    _inherit = 'project.task'

    wbs_code = fields.Char(string='Code WBS (Structure)')
    budget_allocated = fields.Float(string='Budget Alloué')
    cost_materials = fields.Float(string='Coût Matériaux', compute='_compute_actual_costs', store=True)
    cost_labor = fields.Float(string='Coût Main d'œuvre', compute='_compute_actual_costs', store=True)

    @api.depends('material_line_ids', 'timesheet_ids')
    def _compute_actual_costs(self):
        for task in self:
            # Calcul des coûts matières premières issus des réceptions
            task.cost_materials = sum(line.price_subtotal for line in task.material_line_ids)
            # Calcul du coût des feuilles de temps collaborateurs
            task.cost_labor = sum(ts.unit_amount * ts.employee_id.hourly_cost for ts in task.timesheet_ids)
