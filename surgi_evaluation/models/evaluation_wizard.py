from odoo import models, fields, api, _
from odoo.exceptions import UserError, Warning, ValidationError
from datetime import datetime, timedelta, date
import time
from pytz import timezone


class NewModule(models.TransientModel):
    _name = 'evaluation.wizard'

    start_date = fields.Date(string="Start Date", )
    end_date = fields.Date(string="End Date", )
    name=fields.Char(string="Evaluation Name", required=False, )


    employee_ids = fields.Many2many(comodel_name="hr.employee", string="Employees ",)


    def evaluation_create(self):
        print ('+++++++++++++++++++++++++++++++++')
        duration=0.0
        orders_list = []
        if self.employee_ids:
            if self.start_date and self.end_date:
                date_start = datetime.strptime(str(self.start_date), "%Y-%m-%d").date()
                date_end = datetime.strptime(str(self.end_date), "%Y-%m-%d").date()
                print (date_start, date_end, '+++++++++++++++')
                duration = float(str((date_end - date_start).days))


            for rec in self.employee_ids:
                orders_list.append({
                    'name':self.name,
                    'employee_id':rec.id,
                    'date_start':self.start_date,
                    'date_end':self.end_date,
                    'duration':duration,
                    # 'is_evalualtion':True,

                })

                # stock_record = self.env['evaluation.evaluation'].create()

            for i in orders_list:
                print ('iiiiiiiiiiiiiiiii',i)
                self.env['evaluation.evaluation'].sudo().create(i)
