{
    'name': "Calculateur de Commission de Vente",
    'version': "16.1.0",
    'summary': "Moteur de règles complexes calculant les commissions des commerciaux sur la base des marges réelles encaissées.",
    'category': "Accounting",
    'depends': ["base","account","sale","hr"],
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
