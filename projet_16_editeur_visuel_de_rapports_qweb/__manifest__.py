{
    'name': "Éditeur Visuel de Rapports QWeb",
    'version': "17.0.16.0",
    'summary': "Interface intuitive drag-and-drop permettant de personnaliser les factures PDF et bons de commande sans toucher au code XML.",
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
