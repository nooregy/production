# -*- coding: utf-8 -*-
# from odoo import http


# class SurgiEss(http.Controller):
#     @http.route('/surgi_ess/surgi_ess/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/surgi_ess/surgi_ess/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('surgi_ess.listing', {
#             'root': '/surgi_ess/surgi_ess',
#             'objects': http.request.env['surgi_ess.surgi_ess'].search([]),
#         })

#     @http.route('/surgi_ess/surgi_ess/objects/<model("surgi_ess.surgi_ess"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('surgi_ess.object', {
#             'object': obj
#         })
