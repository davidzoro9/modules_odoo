{
    'name': "Application Scan Barcode sur Zebra",
    'version': "17.1.0",
    'summary': "Application mobile Android de scannage rapide de code-barres sur terminaux durcis Zebra pour la validation d'expéditions.",
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
