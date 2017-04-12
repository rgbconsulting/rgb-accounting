# -*- coding: utf-8 -*-
# See README file for full copyright and licensing details.

from openerp import models, api


class PaymentOrder(models.Model):
    _inherit = 'payment.order'

    @api.multi
    def set_done_to_open(self):
        self.bank_line_ids.unlink()
        self.write({'date_done': None})
        self.create_workflow()
        return True
