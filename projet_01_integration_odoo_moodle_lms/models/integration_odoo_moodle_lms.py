# -*- coding: utf-8 -*-
from odoo import models, fields, api

class MoodleConnector(models.AbstractModel):
    _name = 'moodle.connector'
    _description = 'Moodle API Connector'

    def sync_moodle_enrollment(self, student_id, course_id):
        student = self.env['res.partner'].browse(student_id)
        course = self.env['product.product'].search([('moodle_id', '=', course_id)], limit=1)
        if not course:
            raise ValidationError("Le cours Moodle n'existe pas dans le catalogue Odoo.")
        
        # Création de la commande client automatique
        sale_order = self.env['sale.order'].create({
            'partner_id': student.id,
            'order_line': [(0, 0, {
                'product_id': course.id,
                'product_uom_qty': 1.0,
            })]
        })
        sale_order.action_confirm()
        return sale_order.id
