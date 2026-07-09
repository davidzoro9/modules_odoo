{
    'name': "Moteur de Recherche Elasticsearch E-Commerce",
    'version': "16.1.0",
    'summary': "Remplacement de la recherche PostgreSQL par Elasticsearch pour un catalogue e-commerce de 250 000 produits.",
    'category': "Custom",
    'depends': ["base","website"],
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
