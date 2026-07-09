{
    'name': "Portail Candidat RH Interactif",
    'version': "17.1.0",
    'summary': "Développement d'un portail moderne pour le suivi des candidatures de recrutement et le dépôt de pièces justificatives.",
    'category': "Custom",
    'depends': ["base","website","hr"],
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
