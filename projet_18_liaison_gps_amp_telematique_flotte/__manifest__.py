{
    'name': "Liaison GPS &amp; Télématique Flotte",
    'version': "16.1.0",
    'summary': "Intégration des boîtiers GPS Geotab pour remonter automatiquement les kilomètres parcourus et les alertes moteur dans Odoo Fleet.",
    'category': "Technical/API",
    'depends': ["base","fleet"],
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
