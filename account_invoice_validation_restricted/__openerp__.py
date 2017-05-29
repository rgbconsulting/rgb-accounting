# -*- coding: utf-8 -*-
##############################################################################
#
#   Account Invoice Invoicing & Payments Group
#   Copyright 2017 RGB Consulting, SL
#
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU Affero General Public License as
#   published by the Free Software Foundation, either version 3 of the
#   License, or (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU Affero General Public License for more details.
#
#   You should have received a copy of the GNU Affero General Public License
#   along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    'name': "Account Invoice & Payments Validate Restriction",
    'version': '8.0.0.1.0',
    'depends': ['account_accountant'],
    'license': 'AGPL-3',
    'author': "RGB Consulting SL",
    'website': "http://www.rgbconsulting.com",
    'category': ' ',

    'summary': """Account Invoice Invoicing & Payments Group""",

    'description': """
Account Invoice & Payments Validate Restriction
===============================================

This module prevents non accounting users to validate invoices.""",

    'data': [
        'views/account_invoice_views.xml',
    ],

    'demo': [
    ],

    'qweb': [
    ],

}
