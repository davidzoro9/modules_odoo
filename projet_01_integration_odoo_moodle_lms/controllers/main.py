# -*- coding: utf-8 -*-
import json
import logging
from odoo import http
from odoo.http import request

_logger = logging.getLogger(__name__)

class MoodleWebhookController(http.Controller):

    @http.route('/api/moodle/webhook/enroll', type='json', auth='public', methods=['POST'], csrf=False)
    def moodle_webhook_enroll(self, **kwargs):
        """ Webhook endpoint called by Moodle when a student enrolls in a course.
            Expects JSON payload:
            {
                "student_id": 123,
                "course_id": 45
            }
        """
        # Read JSON body
        try:
            data = json.loads(request.httprequest.data)
        except Exception as e:
            return {'status': 'error', 'message': f'Invalid JSON payload: {str(e)}'}

        student_id = data.get('student_id')
        course_id = data.get('course_id')

        if not student_id or not course_id:
            return {'status': 'error', 'message': 'Missing parameters: student_id and course_id are required.'}

        # Check API security token (passed in request headers or body for validation)
        # We fetch config to compare token if required
        config = request.env['moodle.configuration'].sudo().search([('is_active', '=', True)], limit=1)
        if not config:
            return {'status': 'error', 'message': 'Moodle configuration is offline.'}

        # Sync enrollment and create Sales Order
        _logger.info(f"Moodle Webhook Received: Student ID {student_id}, Course ID {course_id}")
        
        # We run the sync method using sudo to bypass user access restrictions
        so_id = request.env['moodle.connector'].sudo().sync_enrollment_records(student_id, course_id)

        if so_id:
            return {
                'status': 'success',
                'message': 'Enrollment processed successfully.',
                'sale_order_id': so_id
            }
        else:
            return {
                'status': 'error',
                'message': 'Failed to process enrollment. Check Odoo synchronization logs.'
            }
