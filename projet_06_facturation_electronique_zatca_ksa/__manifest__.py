{
    'name': "Facturation Électronique ZATCA KSA",
    'version': "16.1.0",
    'summary': "Mise en conformité fiscale complète pour l'Arabie Saoudite (ZATCA Phase 2) avec signature XML et QR codes cryptographiques.",
    'category': "Accounting",
    'depends': ["base","account"],
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
