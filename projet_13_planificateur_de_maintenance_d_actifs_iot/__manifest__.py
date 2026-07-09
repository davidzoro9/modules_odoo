{
    'name': "Planificateur de Maintenance d'Actifs IoT",
    'version': "17.0.15.14",
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
