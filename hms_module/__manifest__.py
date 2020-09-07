# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Hospital Management System',
    'version': '1.1',
    'category': 'business',
    'summary': 'hospital Management system',
    'description': """
This module contains all the common features of hospial management system and hendling.
    """,
    'depends': ['base'],
    'data': [

    'security/ir.model.access.csv',
    'wizard/reject.xml',
    'report/hms_report.xml',
    'view/hms.xml',
    'view/patient.xml',
    'view/extension.xml',
    'view/appointment.xml',
    'view/prescription.xml',
    'data/sequence.xml',
    

        ],
    'demo': [
        
    ],
    'qweb': [
        
    ],
    'installable': True,
    'auto_install': False
}
