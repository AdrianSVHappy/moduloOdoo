# -*- coding: utf-8 -*-
{
    'name': "Laboratotios ASV",

    'summary':  """
	U5_AC_1 - Proyecto final""",

    'description': """
    Modulo del proyecto final de odoo
    """,

    'author': "Adrián Suárez Valdayo",
    'website': "https://edu-glutenfree.odoo.com",
    
    #Indicamos que es una aplicación
	'application': True,

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Productivity',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    # Esto siempre se carga
	'data': [
#   	Este primero indica la politica de acceso del módulo
#   	'security/ir.model.access.csv',
#   	Cargamos las vistas y las plantillas
    	'views/views.xml',
	]

}