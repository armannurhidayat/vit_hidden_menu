# -*- coding: utf-8 -*-
from odoo import http

# class VitHiddenMenu(http.Controller):
#     @http.route('/vit_hidden_menu/vit_hidden_menu/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/vit_hidden_menu/vit_hidden_menu/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('vit_hidden_menu.listing', {
#             'root': '/vit_hidden_menu/vit_hidden_menu',
#             'objects': http.request.env['vit_hidden_menu.vit_hidden_menu'].search([]),
#         })

#     @http.route('/vit_hidden_menu/vit_hidden_menu/objects/<model("vit_hidden_menu.vit_hidden_menu"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('vit_hidden_menu.object', {
#             'object': obj
#         })