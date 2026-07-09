# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import ValidationError

class MoodleConfiguration(models.Model):
    _name = 'moodle.configuration'
    _description = 'Moodle API Configuration'

    name = fields.Char(string="Name", default="Default Moodle Config", required=True)
    moodle_url = fields.Char(string="Moodle URL", required=True, placeholder="https://your-moodle-site.com")
    moodle_token = fields.Char(string="Moodle Web Service Token", required=True)
    is_active = fields.Boolean(string="Active", default=True)

    @api.constrains('is_active')
    def _check_active_config(self):
        # Ensure only one configuration is active at a time
        active_configs = self.search([('is_active', '=', True)])
        if len(active_configs) > 1:
            raise ValidationError("You can only have one active configuration at a time.")

    def sync_courses_action(self):
        self.ensure_one()
        self.env['moodle.connector'].sync_courses()
        # Return a notification message
        return {
            'type': 'ir.actions.client',
            'tag': 'display_notification',
            'params': {
                'title': 'Sync Courses',
                'message': 'Courses synchronization completed successfully.',
                'sticky': False,
                'type': 'success',
            }
        }

    def sync_students_action(self):
        self.ensure_one()
        self.env['moodle.connector'].sync_students()
        return {
            'type': 'ir.actions.client',
            'tag': 'display_notification',
            'params': {
                'title': 'Sync Students',
                'message': 'Students synchronization completed successfully.',
                'sticky': False,
                'type': 'success',
            }
        }
