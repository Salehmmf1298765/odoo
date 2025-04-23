# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'K.S.A. - Payroll Master Report',
    'countries': ['sa'],
    'author': 'Naqlah',
    'website': 'https://www.naqlah.com.sa',
    'category': 'Human Resources/Payroll',
    'version': '1.0',
    'summary': 'Export customized payroll reports for Saudi Arabian companies',
    'icon': '/l10n_sa_hr_payroll_report/static/description/icon.png',
    'description': """
Kingdom of Saudi Arabia Master Payroll Report.
===========================================================
This module adds the master report functionality to the K.S.A. Payroll module.
Provides customized reports formatted according to Saudi standards.
    """,
    'depends': ['hr_payroll', 'l10n_sa_hr_payroll'],
    'data': [
        'security/ir.model.access.csv',
        'views/hr_payroll_master_report_views.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
    'license': 'LGPL-3',
} 