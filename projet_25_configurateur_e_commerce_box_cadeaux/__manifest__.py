{
    'name': "Configurateur E-Commerce Box Cadeaux",
    'version': "17.0.17.0",
    'summary': "Interface e-commerce interactive permettant de composer des paniers gourmands sur-mesure connectés aux stocks d'Odoo.",
    'category': "Custom",
    'depends': ["base","stock","sale","website"],
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
