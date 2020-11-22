from datetime import date
from odoo import api
from odoo import exceptions
from odoo import fields
from odoo import models

class surgi_outdoor_attendance(models.Model):
     _name = 'surgi.outdoor.attendance'
     _inherit = ['mail.thread']
     _order = 'ref'
     # Set refrenced user
     # @api.multi
     def _get_currunt_loged_user(self):
         return self.env.user.id

     employee_name = fields.Many2one(comodel_name='res.users', string="Responsible", default=_get_currunt_loged_user,
                                   track_visibility='onchange')
     ref = fields.Char(string="Ref", related='employee_name.partner_id.ref', readonly=True)
     mobile = fields.Char(string="Mobile", related='employee_name.partner_id.mobile', readonly=True)
     sales_area = fields.Many2one('crm.team', string='Sales Channel', oldname='section_id',
                                   default=lambda self: self.env['crm.team'].search(
                                       ['|', ('user_id', '=', self.env.uid), ('member_ids', '=', self.env.uid)],
                                       limit=1))
     area_manager = fields.Many2one(comodel_name='res.users', string="Area Manager", related='sales_area.user_id',readonly=True)

     operation_id = fields.Many2one('operation.operation', string="Operation", track_visibility='onchange')
     operation_type = fields.Many2one('product.operation.type' ,string="Type",related='operation_id.operation_type',readonly=True)#related='operation_id.operation_type',
     hospital = fields.Many2one('res.partner', string="Hospital",related='operation_id.hospital_id', readonly=True)# related='operation_id.hospital_id',
     surgeon = fields.Many2one('res.partner', string="Surgeon",related='operation_id.surgeon_id', readonly=True)# related='operation_id.surgeon_id',
     op_start_datetime = fields.Datetime('Start DateTime',related='operation_id.start_datetime', readonly=True)#related='operation_id.start_datetime',

     state_employee = fields.Selection(string="", selection=[('operation', 'Operation'), ('mission', 'Mission'),('free','Free') ],)