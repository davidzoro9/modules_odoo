{
    'name': "Connecteur Multi-Transporteurs Global",
    'version': "17.0.17.0",
    'summary': "Intégration API unifiée avec DHL, FedEx, UPS et Colissimo pour le calcul de tarifs réels et l'impression d'étiquettes.",
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
