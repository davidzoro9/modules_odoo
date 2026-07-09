# -*- coding: utf-8 -*-
from odoo import models, fields

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    moodle_course_id = fields.Integer(string="Moodle Course ID", index=True, help="Unique ID of the course on Moodle")
    is_moodle_course = fields.Boolean(string="Is Moodle Course", default=False)
