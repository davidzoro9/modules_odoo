# -*- coding: utf-8 -*-
from odoo import models, fields

class MoodleSyncLog(models.Model):
    _name = 'moodle.sync.log'
    _description = 'Moodle Sync Log'
    _order = 'date desc, id desc'

    name = fields.Char(string="Summary", required=True)
    date = fields.Datetime(string="Sync Date", default=fields.Datetime.now, required=True)
    direction = fields.Selection([
        ('moodle_to_odoo', 'Moodle to Odoo'),
        ('odoo_to_moodle', 'Odoo to Moodle')
    ], string="Direction", required=True)
    sync_type = fields.Selection([
        ('course', 'Courses'),
        ('student', 'Students'),
        ('enrollment', 'Enrollments'),
        ('grade', 'Grades')
    ], string="Sync Type", required=True)
    state = fields.Selection([
        ('success', 'Success'),
        ('failed', 'Failed')
    ], string="Status", default='success', required=True)
    log_details = fields.Text(string="Log Details")
