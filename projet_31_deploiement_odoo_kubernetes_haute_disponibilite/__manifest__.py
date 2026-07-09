{
    'name': "Déploiement Odoo Kubernetes Haute Disponibilité",
    'version': "17.1.0",
    'summary': "Architecture de production scalable sur Azure AKS avec clustering PostgreSQL, instances Odoo stateless et stockage de sessions Redis.",
    'category': "Custom",
    'depends': ["base","mrp","stock"],
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
