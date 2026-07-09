{
    'name': "Gestion Immobilière &amp; Location",
    'version': "15-14.1.0",
    'summary': "Module sur mesure de gestion des baux immobiliers, relances automatiques et facturation automatique des loyers.",
    'category': "Custom",
    'depends': ["base"],
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
