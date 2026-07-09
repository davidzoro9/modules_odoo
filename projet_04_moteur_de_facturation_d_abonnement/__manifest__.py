{
    'name': "Moteur de Facturation d'Abonnement",
    'version': "17.0.15.14",
    'summary': "Moteur de facturation récurrente personnalisé pour services SaaS complexes avec calculs de prorata temporis.",
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
