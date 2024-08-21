# -*- coding: utf-8 -*-
# from odoo import http


# class 21082024(http.Controller):
#     @http.route('/21082024/21082024', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/21082024/21082024/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('21082024.listing', {
#             'root': '/21082024/21082024',
#             'objects': http.request.env['21082024.21082024'].search([]),
#         })

#     @http.route('/21082024/21082024/objects/<model("21082024.21082024"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('21082024.object', {
#             'object': obj
#         })

