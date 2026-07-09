{
    'name': "Chatbot IA Support Client Vectoriel",
    'version': "17.0.17.0",
    'summary': "Intégration d'un agent conversationnel IA exploitant la base de connaissances d'Odoo Helpdesk pour répondre aux requêtes de niveau 1.",
    'category': "Custom",
    'depends': ["base","website"],
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
