# -*- coding: utf-8 -*-
##############################################################################
#
#   Account Move Extended
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
    'name': "Account Move Extended",
    'version': '8.0.1.0.0',
    'depends': ['account'],
    'license': 'AGPL-3',
    'author': "RGB Consulting SL",
    'website': "https://www.rgbconsulting.com",
    'category': 'Account',
    'summary': """Extensions for account moves""",
    'description': """
Account Move Extended
=====================
This module adds extensions to account moves.
    """,

    'data': [
        'views/account_move_line_view.xml',
    ],
}
