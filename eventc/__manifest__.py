  # -*- coding: utf-8 -*-
{
    'name' : 'eventc',
    'version' : '1.1',
    'summary': 'Assignment odoo',
    'sequence': -100,
    'description': """
      Event custom module
     """,
    'category': 'object try',
    'author': 'Abdullah z',
    'website': 'https://abdullah.blogspot.com',
    'images' : [],
    'depends' : ['base','event'],
    'data': [
        'security/ir.model.access.csv',
        'views/sound.xml',
        'views/tagm.xml',
        'views/proj.xml',
        'views/eventc.xml',
        'views/views_menu.xml',
        
        
    ],
    'demo': [],
    'installable': True,
    'active': True,
}