# -*- coding: utf-8 -*-
from odoo import models, fields, api

class CandidatePortalController(http.Controller):
    @http.route(['/my/candidacy'], type='http', auth='user', website=True)
    def my_candidacy(self, **kw):
        partner = request.env.user.partner_id
        applicant = request.env['hr.applicant'].search([('partner_id', '=', partner.id)], limit=1)
        if not applicant:
            return request.redirect('/')
        
        values = {
            'applicant': applicant,
            'stages': request.env['hr.recruitment.stage'].search([]),
        }
        return request.render('candidate_portal.index_template', values)
