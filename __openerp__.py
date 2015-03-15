# -*- coding: utf-8 -*-
{
    'name': "openacademy",

    'summary': """
        modulo de prueba para el curso de odoo de vauxoo""",

    'description': """
        Long description of module's purpose
    """,

    'author': "4geeks",
    'website': "http://www.4geeks.co",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': '4geeks',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'view/openacademy_course_view.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/openacademy_course_demo.xml',
    ],
}