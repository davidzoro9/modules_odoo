{
    'name': "Anonymiseur de Base de Données RGPD",
    'version': "17.0.15.14",
    'summary': "Utilitaire de nettoyage des données nominatives pour la création sécurisée d'environnements de test et staging.",
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
