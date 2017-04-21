# -*- coding: utf-8 -*-
##############################################################################
#
#   Bank statment close
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
    'name': "Bank statment close",
    'version': '8.0.0.1.0',
    'depends': ['account'],
    'license': 'AGPL-3',
    'author': "RGB Consulting SL",
    'website': "http://www.rgbconsulting.com",
    'category': 'Account',
    'summary': """Bank statment close""",
    'description': """
Bank statment close
===========================
This module allows to cancel a bank statement line.
""",

    'data': [
        'views/account_bank_statement.xml',
        'wizard/account_bank_statement_close_warning.xml',
    ],

    'demo': [
    ],

    'qweb': [
    ],
}
