# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.addons import decimal_precision as dp

class HrContract(models.Model):
    _inherit = 'hr.contract'

    @api.depends('increase_2018', 'increase_2017', 'increase_2016', 'increase_2015', 'increase_2014')
    def _getsum_increase_total(self):
        for rec in self:
            rec.increase_total = rec.increase_2018 + rec.increase_2017 + rec.increase_2016 + rec.increase_2015 + rec.increase_2014

    @api.depends('standalone_incentive', 'incentive_2018', 'incentive_2017', 'incentive_2016', 'incentive_2015' ,'incentive_2014')
    def _getsum_incentive_total(self):
        for rec in self:
            rec.incentive_total = rec.standalone_incentive + rec.incentive_2018 + rec.incentive_2017 + rec.incentive_2016 + rec.incentive_2015 + rec.incentive_2014

    @api.depends('basic_salary', 'increase_total')
    def _getsum_salary_total(self):
        for rec in self:
            rec.total_salary_without_incentive = rec.basic_salary + rec.increase_total

    @api.depends('total_salary_without_incentive', 'incentive_total' ,'basic_salary_precent')
    def _getsum_total_salary(self):
        for rec in self:
            rec.total_salary = rec.total_salary_without_incentive + rec.incentive_total + rec.basic_salary_precent

    basic_salary = fields.Float('Basic Wage',track_visibility='onchange',digits=dp.get_precision('Payroll'))
    basic_salary_precent = fields.Float('Basic Salary Precent',track_visibility='onchange',digits=dp.get_precision('Payroll'))
    increase_2018 = fields.Float('2018 Increase.',track_visibility='onchange',digits=dp.get_precision('Payroll'))
    increase_2017 = fields.Float('2017 Increase.',track_visibility='onchange',digits=dp.get_precision('Payroll'))
    increase_2016 = fields.Float('2016 Increase.',track_visibility='onchange',digits=dp.get_precision('Payroll'))
    increase_2015 = fields.Float('2015 Increase.',track_visibility='onchange',digits=dp.get_precision('Payroll'))
    increase_2014 = fields.Float('2014 Increase.',track_visibility='onchange',digits=dp.get_precision('Payroll'))

    increase_total = fields.Float('Total Increase',compute='_getsum_increase_total', track_visibility='onchange')#compute='_getsum_increase_total',

    total_salary_without_incentive = fields.Float('Total salary without incentive',compute='_getsum_salary_total', track_visibility='onchange')#

    standalone_incentive = fields.Float('Standalone Incentive.',track_visibility='onchange',digits=dp.get_precision('Payroll'))
    incentive_2018 = fields.Float('2018 Incentive.',track_visibility='onchange',digits=dp.get_precision('Payroll'))
    incentive_2017 = fields.Float('2017 Incentive.',track_visibility='onchange',digits=dp.get_precision('Payroll'))
    incentive_2016 = fields.Float('2016 Incentive.',track_visibility='onchange',digits=dp.get_precision('Payroll'))
    incentive_2015 = fields.Float('2015 Incentive.',track_visibility='onchange',digits=dp.get_precision('Payroll'))
    incentive_2014 = fields.Float('2014 Incentive.',track_visibility='onchange',digits=dp.get_precision('Payroll'))

    incentive_total = fields.Float('Total Incentive',compute='_getsum_incentive_total', track_visibility='onchange')#compute='_getsum_incentive_total',

    total_salary = fields.Float('Total Salary', compute='_getsum_total_salary', track_visibility='onchange')

    car_allow = fields.Float('Car Allowance',track_visibility='onchange',digits=dp.get_precision('Payroll'))
    fuel_allow = fields.Float('Fuel Allowance',track_visibility='onchange',digits=dp.get_precision('Payroll'))
    # trans_allow = fields.Float('Transportation',track_visibility='onchange',digits=dp.get_precision('Payroll'))
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
