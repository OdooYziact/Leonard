# -*- coding: utf-8 -*-
{
    'name': "licence manager",

    'summary': """
        MODULE DE GESTION DE LICENCE YZIACT""",

    'description': """
        DESCIRIPTION EN + LONG
    """,

    'author': "Yziact",
    'maintainer': '',
    'website': "http://gitlab.yziact.net/odoo/commons/module",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': [
        'base',
        'product',
        'stock',
        'sale_subscription',
        'purchase',
        'account'
    ],

    # always loaded
    'data': [
        'views/product_views.xml',
        'views/product_licence_2.xml',
        #'views/views.xml',
        #'views/templates.xml',
        'security/ir.model.access.csv',
    ],
}
