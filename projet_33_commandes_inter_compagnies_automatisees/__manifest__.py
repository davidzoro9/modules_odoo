{
    'name': "Commandes Inter-Compagnies Automatisées",
    'version': "17.1.0",
    'summary': "Génération automatique d'un bon de commande fournisseur (PO) lorsqu'une filiale valide un bon de commande client (SO).",
    'category': "Custom",
    'depends': ["base","sale","purchase"],
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
