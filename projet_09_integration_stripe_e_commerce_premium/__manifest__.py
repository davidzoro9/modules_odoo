{
    'name': "Intégration Stripe E-Commerce Premium",
    'version': "17.1.0",
    'summary': "Mise en place de Stripe Payment Element avec gestion des abonnements, Apple Pay, Google Pay et 3D Secure v2.",
    'category': "Technical/API",
    'depends': ["base","sale","website"],
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
