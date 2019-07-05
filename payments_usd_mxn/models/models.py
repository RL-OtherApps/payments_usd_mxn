# -*- coding: utf-8 -*-

from odoo import models, fields, api

class wizar_paGOS_USD_MXN(models.Model):
    _name = 'wizar.usd.mxn'

    name = fields.Char(string="name")

    payment_type = fields.Selection([('outbound', 'Send Money'), ('inbound', 'Receive Money'),('transfer', 'Internal Transfer')],string ="Tipo de pago") 

    @api.multi
    def pagos(self):
        self.ensure_one()
        if self.payment_type :
            dom =[]
            title_sel = ""
            if self.payment_type == 'outbound':
                dom = [('payment_type','=','outbound')]
                title_sel = ' de Enviar Dinero'
            elif self.payment_type == 'inbound':
                dom = [('payment_type','=', 'inbound')]
                title_sel = ' de Recibir Dinero'

            elif self.payment_type == 'transfer':
                dom = [('payment_type', '=' , 'transfer' )] 
                title_sel = " de Trasferencia Interna"       
            else:
                dom = [] 
                title_sel = ' General '


            tree_view_id = self.env.ref('payments_usd_mxn.id_view_historial_pagos_tree').id

            action = {
                'type': 'ir.actions.act_window',
                'views': [(tree_view_id, 'tree')],
                'view_mode': 'tree',
                'name': ('Historial' + str(title_sel)),
                'res_model': 'account.payment',
                'domain':  dom
            }
            return action


class camposNuevos(models.Model):
    _inherit = 'account.payment'

    importe_mxn = fields.Monetary(string="Importe MXN")
    importe_usd = fields.Monetary(string ="Importe USD")



    @api.onchange('amount')
    def compute_importe_usd_mxn(self):
        self.ensure_one()
        self.importe_usd = self.env['res.currency']._compute(self.currency_id, self.env['res.currency'].search([('name','=','USD')], limit=1), self.amount)
        self.importe_mxn = self.env['res.currency']._compute(self.currency_id, self.env['res.currency'].search([('name','=','MXN')], limit=1), self.amount)

        





