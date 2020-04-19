# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.addons import decimal_precision as dp

class HrContract(models.Model):
    _inherit = 'hr.contract'

    # @api.onchange('increase_2018', 'increase_2017', 'increase_2016', 'increase_2015', 'increase_2014')
    # def _getsum_increase_total(self):
    #     if self.increase_2018 or self.increase_2017 or self.increase_2016 or self.increase_2015 or self.increase_2014:
    #         self.increase_total = self.increase_2018 + self.increase_2017 + self.increase_2016 + self.increase_2015 + self.increase_2014

    # @api.onchange('standalone_incentive', 'incentive_2018', 'incentive_2017', 'incentive_2016', 'incentive_2015' ,'incentive_2014')
    # def _getsum_incentive_total(self):
    #     if self.standalone_incentive or self.incentive_2018 or self.incentive_2017 or self.incentive_2016 or self.incentive_2015 or self.incentive_2014 :
    #         self.incentive_total = self.standalone_incentive + self.incentive_2018 + self.incentive_2017 + self.incentive_2016 + self.incentive_2015 + self.incentive_2014

    # @api.onchange('basic_salary', 'increase_total')
    # def _getsum_salary_total(self):
    #     if self.basic_salary or self.increase_total:
    #         self.total_salary_without_incentive = self.basic_salary + self.increase_total

    basic_salary = fields.Float('Basic Wage',track_visibility='onchange',digits=dp.get_precision('Payroll'))
    basic_salary_precent = fields.Float('Basic Salary Precent',track_visibility='onchange',digits=dp.get_precision('Payroll'))
    increase_2018 = fields.Float('2018 Increase.',track_visibility='onchange',digits=dp.get_precision('Payroll'))
    increase_2017 = fields.Float('2017 Increase.',track_visibility='onchange',digits=dp.get_precision('Payroll'))
    increase_2016 = fields.Float('2016 Increase.',track_visibility='onchange',digits=dp.get_precision('Payroll'))
    increase_2015 = fields.Float('2015 Increase.',track_visibility='onchange',digits=dp.get_precision('Payroll'))
    increase_2014 = fields.Float('2014 Increase.',track_visibility='onchange',digits=dp.get_precision('Payroll'))
    # increase_total = fields.Float('Total Increase', compute='_getsum_increase_total',track_visibility='onchange')
    # total_salary_without_incentive = fields.Float('Total salary without incentive', compute='_getsum_salary_total',track_visibility='onchange')
    standalone_incentive = fields.Float('Standalone Incentive.',track_visibility='onchange',digits=dp.get_precision('Payroll'))
    incentive_2018 = fields.Float('2018 Incentive.',track_visibility='onchange',digits=dp.get_precision('Payroll'))
    incentive_2017 = fields.Float('2017 Incentive.',track_visibility='onchange',digits=dp.get_precision('Payroll'))
    incentive_2016 = fields.Float('2016 Incentive.',track_visibility='onchange',digits=dp.get_precision('Payroll'))
    incentive_2015 = fields.Float('2015 Incentive.',track_visibility='onchange',digits=dp.get_precision('Payroll'))
    incentive_2014 = fields.Float('2014 Incentive.',track_visibility='onchange',digits=dp.get_precision('Payroll'))
    # incentive_total = fields.Float('Total Incentive', compute='_getsum_incentive_total',track_visibility='onchange')
    car_allow = fields.Float('Car Allowance',track_visibility='onchange',digits=dp.get_precision('Payroll'))
    fuel_allow = fields.Float('Fuel Allowance',track_visibility='onchange',digits=dp.get_precision('Payroll'))
    trans_allow = fields.Float('Transportation',track_visibility='onchange',digits=dp.get_precision('Payroll'))
    trans_allow_mokattam = fields.Float('Transportation Mokattam',track_visibility='onchange',digits=dp.get_precision('Payroll'))
    trans_allow_bank = fields.Float('Transportation Bank',track_visibility='onchange',digits=dp.get_precision('Payroll'))
    travel_expenses_allow = fields.Float('Travel Exp Allow.',track_visibility='onchange',digits=dp.get_precision('Payroll'))
    hazard_pay = fields.Float('Hazard Pay',track_visibility='onchange',digits=dp.get_precision('Payroll'))
    travel_allow_int_f = fields.Float('Travel Allow internal Fixed',track_visibility='onchange',digits=dp.get_precision('Payroll'))
    advance_sales_comm = fields.Float('Advanced Sales Commissions',track_visibility='onchange',digits=dp.get_precision('Payroll'))
    advance_collection_comm = fields.Float('Advanced Collection Commissions',track_visibility='onchange',digits=dp.get_precision('Payroll'))
    mobi = fields.Float('Mobile',track_visibility='onchange',digits=dp.get_precision('Payroll'))
    housing = fields.Float('Housing Allowance',track_visibility='onchange',digits=dp.get_precision('Payroll'))
    nature = fields.Float('Nature Of Work',track_visibility='onchange',digits=dp.get_precision('Payroll'))
