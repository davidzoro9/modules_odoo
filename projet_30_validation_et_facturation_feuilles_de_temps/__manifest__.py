{
    'name': "Validation et Facturation Feuilles de Temps",
    'version': "17.0.15.14",
    'summary': "Workflow de validation multi-niveaux des feuilles de temps collaborateurs avant émission des factures clients.",
    'category': "Accounting",
    'depends': ["base","account","hr"],
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
