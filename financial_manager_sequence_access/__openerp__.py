# -*- coding: utf-8 -*-
##############################################################################
#
#   Financial Manager Sequence Access
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
    'name': "Financial Manager Sequence Access",
    'version': '8.0.0.1.0',
    'depends': ['base','account'],
    'license': 'AGPL-3',
    'author': "RGB Consulting SL",
    'website': "http://www.rgbconsulting.com",
    'category': 'Account',
    'summary': """Financial Manager Sequence Access""",
    'description': """
Financial Manager Sequence Access
=================================
Add permisions to financial manager group to allow to edit sequences.
""",

    'data': [
        'security/ir.model.access.csv',
    ],

    'demo': [
    ],

    'qweb': [
    ],
}
