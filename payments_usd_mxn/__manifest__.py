# -*- coding: utf-8 -*-
{
    'name': "payments_usd_mxn",

    'summary': """
    payments_usd_mxn: Look for the payment history of customers and suppliers to pay, the same way converts the amount to be paid in USD and MXN currency.""",

    'description': """
        
    Look for the payment history of customers and suppliers to pay
            """,
    'author': "XMARTS",
    'email': 'desarrollo@xmarts.com',
    'website': "https://xmarts.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','account'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],

    'installable': True,
    'application': True,
}