{
    'name': "Migration Odoo v14 à v17 Enterprise",
    'version': "17.1.0",
    'summary': "Migration complète d'une base de données Odoo de 500 Go comptant 45 modules personnalisés et 12 ans d'historique.",
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
