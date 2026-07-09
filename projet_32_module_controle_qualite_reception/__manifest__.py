{
    'name': "Module Contrôle Qualité Réception",
    'version': "17.0.16.0",
    'summary': "Formulaires de contrôle qualité personnalisés obligatoires lors de la réception de matières premières critiques avec signature électronique.",
    'category': "Custom",
    'depends': ["base","stock"],
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
