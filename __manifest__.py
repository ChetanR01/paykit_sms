{
    'name': 'Prisms SMS Gateway',
    'version' : "1.0",
    'author' : "Prisms",
    'website':'https://prisms.in',
    'summary': "Prisms sms module",
    'category':'Marketing',
    'description': "SMS Gateway",
    'depends' : ['base'],
    'data': [
        # 'views/sms_server_view.xml',
        'views/sms_template_view.xml',

        'security/ir.model.access.csv',
    ],

    'assets': {
        'web.assets_frontend': [ 
        ],
    },
    'price': 50,
    'currency': 'USD',
    'installable': True,
    'application' : True,
    'license': 'LGPL-3',
}
