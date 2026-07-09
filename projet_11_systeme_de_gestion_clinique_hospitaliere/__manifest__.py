{
    'name': "Système de Gestion Clinique Hospitalière",
    'version': "17.1.0",
    'summary': "Dossier médical patient (EHR), planification des consultations de médecins et facturation des actes médicaux.",
    'category': "Custom",
    'depends': ["base","hr"],
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
