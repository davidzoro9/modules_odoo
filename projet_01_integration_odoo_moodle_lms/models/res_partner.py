# -*- coding: utf-8 -*-
from odoo import models, fields

class ResPartner(models.Model):
    _inherit = 'res.partner'

    moodle_user_id = fields.Integer(string="Moodle User ID", index=True, help="Unique ID of the student on Moodle")
    is_moodle_student = fields.Boolean(string="Is Moodle Student", default=False)
