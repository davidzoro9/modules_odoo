# -*- coding: utf-8 -*-
{
    'name': "Intégration Odoo - Moodle LMS",
    'version': "17.1.0",
    'summary': "Synchronisation bidirectionnelle automatique des inscriptions, cours, et notes entre la plateforme Moodle et l'ERP Odoo.",
    'category': "Technical/API",
    'depends': ['base', 'product', 'sale'],
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
