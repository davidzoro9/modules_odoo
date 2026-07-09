{
    'name': "Application Client Mobile (Flutter)",
    'version': "17.1.0",
    'summary': "Développement d'une application iOS &amp; Android en Flutter connectée à Odoo pour le suivi des commandes et tickets de support B2B.",
    'category': "Technical/API",
    'depends': ["base"],
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
