odoo.define('emp_attendance_google_map_app.my_attendances_restriction', function (require) {
"use strict";

	var AbstractAction = require('web.AbstractAction');
	var core = require('web.core');
	var ajax = require('web.ajax');
	var MyAttendances = require('hr_attendance.my_attendances');
	var GreetingMessage = require('hr_attendance.greeting_message')
	var QWeb = core.qweb;
	var _t = core._t;
	var rpc = require('web.rpc');
	var field_utils = require('web.field_utils');

	MyAttendances.include({

		willStart: function () {
	        var self = this;

	        var def = this._rpc({
	                model: 'hr.employee',
	                method: 'search_read',
	                args: [[['user_id', '=', this.getSession().uid]], ['attendance_state', 'name', 'hours_today']],
	            })
	            .then(function (res) {
	                self.employee = res.length && res[0];
	                if (res.length) {
	                    self.hours_today = field_utils.format.float_time(self.employee.hours_today);
	                }
	            });
	        return Promise.all([def, this._super.apply(this, arguments)]);
	    },

		update_attendance: function () {
        var self = this;
        var co_o = [];
        navigator.geolocation.getCurrentPosition(function(position){
			self.lat = position.coords.latitude;
			self.long = position.coords.longitude;
	        rpc.query({
	                model: 'hr.employee',
	                method: 'attendance_manual',
	                args: [[self.employee.id], 'hr_attendance.hr_attendance_action_my_attendances', self.lat, self.long],
	            })
	            .then(function(result) {
	                if (result.action) {
	                    self.do_action(result.action);
	                } else if (result.warning) {
	                    self.do_warn(result.warning);
	                }
	            });
            });	
    	},
	});
});