{
    'name': "Terminal POS Restaurant sur Tablette",
    'version': "17.0.18.0",
    'summary': "Interface tactile hors-ligne optimisée pour la prise de commande aux tables par les serveurs.",
    'category': "Custom",
    'depends': ["base","sale"],
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
