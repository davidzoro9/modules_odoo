{
    'name': "Connecteur OData PowerBI - Odoo",
    'version': "17.0.17.0",
    'summary': "Exposition de modèles Odoo en flux OData sécurisés pour alimenter en direct des rapports décisionnels PowerBI.",
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
