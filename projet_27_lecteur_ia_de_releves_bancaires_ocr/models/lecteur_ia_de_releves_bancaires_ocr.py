# -*- coding: utf-8 -*-
from odoo import models, fields, api

class BankStatementImport(models.TransientModel):
    _inherit = 'account.bank.statement.import'

    def parse_pdf_via_ocr(self, pdf_file):
        # Envoi au service de Deep Learning OCR
        ocr_service_url = "https://api.ocr-accounting.com/v1/extract"
        response = requests.post(ocr_service_url, files={'file': pdf_file})
        if response.status_code == 200:
            extracted_lines = response.json().get('transactions', [])
            statement_lines = []
            for line in extracted_lines:
                statement_lines.append({
                    'date': line['date'],
                    'name': line['description'],
                    'amount': float(line['amount'])
                })
            return statement_lines
        return []
