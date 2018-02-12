# -*- coding: utf-8 -*-
# See README file for full copyright and licensing details.

from openerp import api, fields, models


class AccountInvoice(models.Model):
    _inherit = 'account.invoice'

    global_amount_untaxed = fields.Float(string="Subtotal", store=True, compute='_compute_global_amounts')
    global_amount_total = fields.Float(string="Total", store=True, compute='_compute_global_amounts')
    global_residual = fields.Float(string="Balance", store=True, compute='_compute_global_amounts')

    @api.one
    @api.depends('type', 'amount_untaxed', 'amount_total', 'residual')
    def _compute_global_amounts(self):
        # Compute global amount untaxed
        if self.amount_untaxed:
            if self.type in ('in_refund', 'out_refund'):
                self.global_amount_untaxed = self.amount_untaxed * -1
            else:
                self.global_amount_untaxed = self.amount_untaxed
        else:
            self.x_amount_untaxed = 0.0
        # Compute global amount total
        if self.amount_total:
            if self.type in ('in_refund', 'out_refund'):
                self.global_amount_total = self.amount_total * -1
            else:
                self.global_amount_total = self.amount_total
        else:
            self.global_amount_total = 0.0
        # Compute global residual
        if self.residual:
            if self.type in ('in_refund', 'out_refund'):
                self.global_residual = self.residual * -1
            else:
                self.global_residual = self.residual
        else:
            self.global_residual = 0
