{
    'name': "Portail Fournisseur &amp; Enchères RFQ",
    'version': "16.1.0",
    'summary': "Espace sécurisé de négociation où les sous-traitants répondent aux demandes de prix (RFQ) et déposent leurs devis.",
    'category': "Custom",
    'depends': ["base","website","purchase"],
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
