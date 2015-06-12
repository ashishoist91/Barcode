# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################


{
    'name': 'Products Barcode Print',
    'version': '1.1',
    'author': 'Logicious',
    'category': 'Sales Management',
    'depends': ['product', 'report'],
    'demo': [],
    'website': 'https://www.logicious.net',
    'description': """
This is the  module for printing bracode.
========================================================================

Print product labels with barcode.
    """,
    'data': [
        'product_barcode_report.xml',
        'views/report_paperformat.xml',
        'views/report_product_barcode.xml',
    ],
    'test': [],
    'installable': True,
    'auto_install': False,
    'images': [],
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
