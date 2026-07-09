{
    'name': "Lecteur IA de Relevés Bancaires OCR",
    'version': "16.1.0",
    'summary': "Intégration de modèles de Deep Learning pour l'analyse OCR et le rapprochement comptable automatique des relevés bancaires PDF complexes.",
    'category': "Accounting",
    'depends': ["base","account","mrp"],
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
