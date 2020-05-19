# -*- coding: utf-8 -*-
from odoo import api, fields, models, _

class AccountInvoiceInherit(models.Model):
    _inherit = 'account.move'

    customer_printed_name = fields.Char(string="Customer Printed Name")
    sales_area_manager = fields.Many2one(comodel_name='res.users', string="Area Manager", related='team_id.user_id',
                                         readonly=True)
    collection_rep = fields.Many2one('res.users', 'Collection Rep', track_visibility='onchange')

    invoice_printing_description = fields.Text('Invoice Printing Description')
    print_description = fields.Boolean('Print Description', default=False)
    exchange_invoices = fields.Boolean("Exchanged invoices")
    exchange_invoices_id = fields.Many2one('account.move', 'Exchange invoices No.')
