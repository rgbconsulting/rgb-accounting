# -*- coding: utf-8 -*-
# See README file for full copyright and licensing details.

from openerp import models, api, fields


class AccountBankStatementLine(models.Model):
    _inherit = 'account.bank.statement.line'

    active = fields.Boolean('Active', default=True)
