# -*- coding: utf-8 -*-
import requests
import logging
from odoo import models, fields, api
from odoo.exceptions import UserError

_logger = logging.getLogger(__name__)

class MoodleConnector(models.AbstractModel):
    _name = 'moodle.connector'
    _description = 'Moodle API Connector Service'

    def _get_config(self):
        config = self.env['moodle.configuration'].search([('is_active', '=', True)], limit=1)
        if not config:
            raise UserError("No active Moodle configuration found. Please configure the connection settings.")
        return config

    def _call_moodle_api(self, wsfunction, params=None):
        config = this = self._get_config()
        url = f"{config.moodle_url.rstrip('/')}/webservice/rest/server.php"
        
        default_params = {
            'wstoken': config.moodle_token,
            'wsfunction': wsfunction,
            'moodlewsrestformat': 'json'
        }
        if params:
            default_params.update(params)

        try:
            response = requests.post(url, data=default_params, timeout=15)
            response.raise_for_status()
            res_data = response.json()
            
            # Handle Moodle-specific API errors
            if isinstance(res_data, dict) and res_data.get('exception'):
                raise UserError(f"Moodle Web Service Exception: {res_data.get('message')}")
            return res_data
        except requests.exceptions.RequestException as e:
            raise UserError(f"Network error trying to connect to Moodle API: {str(e)}")

    def sync_courses(self):
        """ Fetch courses from Moodle and register them as products in Odoo """
        try:
            courses_data = self._call_moodle_api('core_course_get_courses')
            created_count = 0
            updated_count = 0

            for course in courses_data:
                # Skip the default site home course (usually ID 1)
                if course.get('id') == 1:
                    continue

                moodle_id = course.get('id')
                name = course.get('fullname')
                summary = course.get('summary') or ''

                product = self.env['product.template'].search([('moodle_course_id', '=', moodle_id)], limit=1)
                vals = {
                    'name': name,
                    'list_price': 0.0,  # Default price, user can change it
                    'is_moodle_course': True,
                    'moodle_course_id': moodle_id,
                    'detailed_type': 'service'
                }

                if product:
                    product.write(vals)
                    updated_count += 1
                else:
                    self.env['product.template'].create(vals)
                    created_count += 1

            self.env['moodle.sync.log'].create({
                'name': 'Course Synchronization Success',
                'direction': 'moodle_to_odoo',
                'sync_type': 'course',
                'state': 'success',
                'log_details': f"Successfully synchronized courses. Created: {created_count}, Updated: {updated_count}."
            })
            return True
        except Exception as e:
            self.env['moodle.sync.log'].create({
                'name': 'Course Synchronization Failed',
                'direction': 'moodle_to_odoo',
                'sync_type': 'course',
                'state': 'failed',
                'log_details': str(e)
            })
            raise UserError(f"Failed to sync courses: {str(e)}")

    def sync_students(self):
        """ Fetch Moodle users and create/update Odoo Partners """
        try:
            # Fetch all users (simplification: custom SQL or web service can filter by role)
            # Moodle Web Service function: core_user_get_users_by_field
            # Since moodle doesn't have a direct 'get all users' WS function without filters,
            # we request by search parameter or filter. Typically, schools query based on custom criteria.
            # We mock the params for retrieving users with ID > 0.
            users_data = self._call_moodle_api('core_user_get_users', {
                'criteria[0][key]': 'id',
                'criteria[0][value]': '0',
                'criteria[0][comparison]': '>'
            })
            
            users = users_data.get('users', [])
            created_count = 0
            updated_count = 0

            for user in users:
                moodle_id = user.get('id')
                email = user.get('email')
                firstname = user.get('firstname')
                lastname = user.get('lastname')
                fullname = f"{firstname} {lastname}"

                partner = self.env['res.partner'].search([('moodle_user_id', '=', moodle_id)], limit=1)
                if not partner and email:
                    # Fallback lookup by email to prevent duplicates
                    partner = self.env['res.partner'].search([('email', '=', email)], limit=1)

                vals = {
                    'name': fullname,
                    'email': email,
                    'is_moodle_student': True,
                    'moodle_user_id': moodle_id,
                }

                if partner:
                    partner.write(vals)
                    updated_count += 1
                else:
                    self.env['res.partner'].create(vals)
                    created_count += 1

            self.env['moodle.sync.log'].create({
                'name': 'Student Synchronization Success',
                'direction': 'moodle_to_odoo',
                'sync_type': 'student',
                'state': 'success',
                'log_details': f"Successfully synchronized students. Created: {created_count}, Updated: {updated_count}."
            })
            return True
        except Exception as e:
            self.env['moodle.sync.log'].create({
                'name': 'Student Synchronization Failed',
                'direction': 'moodle_to_odoo',
                'sync_type': 'student',
                'state': 'failed',
                'log_details': str(e)
            })
            raise UserError(f"Failed to sync students: {str(e)}")

    def sync_enrollment_records(self, moodle_student_id, moodle_course_id):
        """ Triggered by webhook or scheduled cron job:
            Create a Sales Order in Odoo for a Moodle enrollment.
        """
        try:
            # Find the Odoo Partner and Product
            partner = self.env['res.partner'].search([('moodle_user_id', '=', moodle_student_id)], limit=1)
            product = self.env['product.product'].search([('moodle_course_id', '=', moodle_course_id)], limit=1)

            if not partner:
                raise UserError(f"Cannot sync enrollment: No partner found in Odoo for Moodle User ID {moodle_student_id}.")
            if not product:
                raise UserError(f"Cannot sync enrollment: No product found in Odoo for Moodle Course ID {moodle_course_id}.")

            # Check if Sales Order already exists for this enrollment to avoid duplicates
            existing_so = self.env['sale.order'].search([
                ('partner_id', '=', partner.id),
                ('order_line.product_id', '=', product.id)
            ], limit=1)

            if existing_so:
                return existing_so.id

            # Create the Sales Order
            sale_order = self.env['sale.order'].create({
                'partner_id': partner.id,
                'order_line': [(0, 0, {
                    'product_id': product.id,
                    'product_uom_qty': 1.0,
                    'price_unit': product.list_price,
                })]
            })
            sale_order.action_confirm()

            self.env['moodle.sync.log'].create({
                'name': f"Enrollment Sync Success (SO: {sale_order.name})",
                'direction': 'moodle_to_odoo',
                'sync_type': 'enrollment',
                'state': 'success',
                'log_details': f"Automatically enrolled student {partner.name} into course {product.name}. Created SO {sale_order.name}."
            })
            return sale_order.id
        except Exception as e:
            self.env['moodle.sync.log'].create({
                'name': 'Enrollment Sync Failed',
                'direction': 'moodle_to_odoo',
                'sync_type': 'enrollment',
                'state': 'failed',
                'log_details': f"Student ID: {moodle_student_id}, Course ID: {moodle_course_id}. Error: {str(e)}"
            })
            _logger.error(f"Odoo Moodle Enrollment Sync Error: {str(e)}")
            return False
