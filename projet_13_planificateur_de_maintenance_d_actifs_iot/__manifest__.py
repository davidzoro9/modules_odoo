{
    'name': "Planificateur de Maintenance d'Actifs IoT",
    'version': "15-14.1.0",
    'summary': "Gestion prévisionnelle de maintenance d'équipements industriels basée sur les heures de fonctionnement réelles issues de capteurs IoT.",
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
