# -*- coding: utf-8 -*-

##############################################################################
#    Copyright (C) 2020.
#    Author: Eng.Ramadan Khalil (<rkhalil1990@gmail.com>)
#    website': https://www.linkedin.com/in/ramadan-khalil-a7088164
#
#    It is forbidden to publish, distribute, sublicense, or sell copies
#    of the Software or modified copies of the Software.
##############################################################################

from odoo import api, fields, models, _
from odoo.exceptions import ValidationError, UserError


class HrAttendancePolicy(models.Model):
    _inherit = 'hr.attendance.policy'

    def get_late(self,period, cnt):
        res = period
        flag = False
        no = 1
        cnt_flag = False
        factor = 1
        if period <= 0:
            return 0, cnt
        if self.late_rule_id:
            time_ids = self.late_rule_id.line_ids.sorted(
                key=lambda r: r.time, reverse=True)
            for line in time_ids:
                if period >= line.time:
                    for counter in cnt:
                        if counter[0] == line.time:
                            cnt_flag = True
                            no = counter[1]
                            counter[1] += 1
                            break
                    if no >= 5 and line.fifth > 0:
                        factor = line.fifth
                    elif no >= 4 and line.fourth > 0:
                        factor = line.fourth
                    elif no >= 3 and line.third > 0:
                        factor = line.third
                    elif no >= 2 and line.second > 0:
                        factor = line.second
                    elif no >= 1 and line.first > 0:
                        factor = line.first
                    elif no == 0:
                        factor = 0
                    if not cnt_flag:
                        cnt.append([line.time, 2])
                    flag = True
                    if line.type == 'rate':
                        res = line.rate * period * factor
                    elif line.type == 'fix':
                        res = line.amount * factor

                    break

            if not flag:
                res = 0
        return res, cnt

    def get_diff(self, period, diff_cnt):
        res = period
        flag = False
        no = 1
        cnt_flag = False
        factor = 1
        if period <= 0:
            return 0, diff_cnt
        if self.diff_rule_id:
            time_ids = self.diff_rule_id.line_ids.sorted(
                key=lambda r: r.time, reverse=True)
            for line in time_ids:
                if period >= line.time:
                    for counter in diff_cnt:
                        if counter[0] == line.time:
                            cnt_flag = True
                            no = counter[1]
                            counter[1] += 1
                            break
                    if no >= 5:
                        factor = line.fifth
                    elif no >= 4:
                        factor = line.fourth
                    elif no >= 3:
                        factor = line.third
                    elif no >= 2:
                        factor = line.second
                    elif no >= 1:
                        factor = line.first
                    elif no >= 0:
                        factor = 1
                    if not cnt_flag:
                        diff_cnt.append([line.time, 2])
                    flag = True
                    if line.type == 'rate':
                        res = line.rate * period * factor
                    elif line.type == 'fix':
                        res = line.amount * factor
                    break
            if not flag:
                res = 0
        return res, diff_cnt

class HrLateRuleLine(models.Model):
    _inherit = 'hr.late.rule.line'

    first = fields.Float('First Time', default=1)
    second = fields.Float('Second Time', default=1)
    third = fields.Float('Third Time', default=1)
    fourth = fields.Float('Fourth Time', default=1)
    fifth = fields.Float('Fifth Time', default=1)


class HrDiffRuleLine(models.Model):
    _inherit = 'hr.diff.rule.line'

    first = fields.Float('First Time', default=1)
    second = fields.Float('Second Time', default=1)
    third = fields.Float('Third Time', default=1)
    fourth = fields.Float('Fourth Time', default=1)
    fifth = fields.Float('Fifth Time', default=1)



