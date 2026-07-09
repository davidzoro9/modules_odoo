{
    'name': "Synchronisation HubSpot CRM - Odoo",
    'version': "17.0.15.14",
    'summary': "Connecteur complet pour l'envoi asynchrone des leads marketing HubSpot vers le pipeline de ventes Odoo.",
    'category': "Technical/API",
    'depends': ["base","hr"],
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
