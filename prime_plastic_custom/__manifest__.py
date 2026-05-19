# -*- coding: utf-8 -*-
{
    "name": "Prime Plastic Custom",

    'version': '19.0.0.0',

    'summary': """Prime Plastic Custom""",


    'description': """Prime Plastic Custom""",

    'category': 'all',

    'author': "SelectaSol",

    'website': 'https://selectasol.com',

    "depends": ['base', 'stock','product','sale','purchase'],

    "data": [
        'security/ir.model.access.csv',
        'views/colors_views.xml',
        'views/product_model_views.xml',
        'views/material_views.xml',
        'views/product_template_views.xml',
    ],

    'license': 'LGPL-3',
    'installable': True,
    'auto_install': False,
}
