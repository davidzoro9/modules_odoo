{
    'name': "Connecteur Shopify Bi-Directionnel",
    'version': "17.0.17.0",
    'summary': "Synchronisation automatique des stocks de sécurité, images, attributs produits et ventes entre Shopify et Odoo.",
    'category': "Technical/API",
    'depends': ["base","stock","hr"],
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
