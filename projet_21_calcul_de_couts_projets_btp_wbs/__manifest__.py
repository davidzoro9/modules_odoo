{
    'name': "Calcul de Coûts Projets BTP (WBS)",
    'version': "17.0.16.0",
    'summary': "Extension du module projet d'Odoo avec structure WBS multi-niveaux pour le suivi des coûts réels de chantiers de construction.",
    'category': "Custom",
    'depends': ["base","account"],
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
