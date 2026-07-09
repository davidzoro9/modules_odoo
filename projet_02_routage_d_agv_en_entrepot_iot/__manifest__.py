{
    'name': "Routage d'AGV en Entrepôt IoT",
    'version': "17.0.16.0",
    'summary': "Connexion d'Odoo Inventory à des robots logistiques AGV pour l'optimisation des parcours de picking en temps réel.",
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
