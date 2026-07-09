{
    'name': "Planificateur Ordonnancement Gantt MRP",
    'version': "17.1.0",
    'summary': "Vue Gantt drag-and-drop interactive pour la planification fine des capacités des centres de travail.",
    'category': "Custom",
    'depends': ["base","mrp"],
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
