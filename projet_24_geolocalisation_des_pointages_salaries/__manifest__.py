{
    'name': "Géolocalisation des Pointages Salariés",
    'version': "16.1.0",
    'summary': "Contrôle de conformité de pointage horaire basé sur la géolocalisation GPS du mobile des techniciens itinérants.",
    'category': "Custom",
    'depends': ["base","fleet","hr"],
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
