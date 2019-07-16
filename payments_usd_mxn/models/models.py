# -*- coding: utf-8 -*-

from odoo import models, fields, api

class wizar_paGOS_USD_MXN(models.Model):
    _name = 'wizar.usd.mxn'

    name = fields.Char(string="name")

   # type = fields.Selection([('outbound', 'Send Money'), ('inbound', 'Receive Money'),('transfer', 'Internal Transfer')],string ="Tipo de pago")

    type = fields.Selection([('out_invoice','Factura de Cliente'), ('in_invoice','Factura de Vendedor')],) 

    @api.multi
    def pagos(self):
        self.ensure_one()
        if self.type :
            dom =[]
            title_sel = ""
            if self.type == 'out_invoice':
                dom = [('type','=','out_invoice')]
                title_sel = ' por  Cliente'

            elif self.type == 'in_invoice':
                dom = [('type', '=' , 'in_invoice' )] 
                title_sel = " por Proveedor"       
            else:
                dom = [] 
                title_sel = ' General '


            tree_view_id = self.env.ref('payments_usd_mxn.id_view_historial_pagos_tree').id

            action = {
                'type': 'ir.actions.act_window',
                'views': [(tree_view_id, 'tree')],
                'view_mode': 'tree',
                'name': ('Factura' + str(title_sel)),
                'res_model': 'account.invoice',
                'domain':  dom
            }
            return action


class camposNuevos(models.Model):
    _inherit = 'account.invoice' 

    importe_mxn = fields.Monetary(string="Total MXN")
    importe_usd = fields.Monetary(string ="Total USD")

    mxn = fields.Monetary(string="Pagar MXN", compute="_funcion")
    usd = fields.Monetary(string="Pagar USD", compute="_funcion")


    @api.one
    def _funcion(self):
        if self.residual:
            self.usd = self.env['res.currency']._compute(self.currency_id, self.env['res.currency'].search([('name','=','USD')], limit=1), self.residual)
            self.mxn = self.env['res.currency']._compute(self.currency_id, self.env['res.currency'].search([('name','=','MXN')], limit=1), self.residual)

    @api.onchange('amount_total')
    def compute_importe_usd_mxn(self):
        self.ensure_one()
        self.importe_usd = self.env['res.currency']._compute(self.currency_id, self.env['res.currency'].search([('name','=','USD')], limit=1), self.amount_total)
        self.importe_mxn = self.env['res.currency']._compute(self.currency_id, self.env['res.currency'].search([('name','=','MXN')], limit=1), self.amount_total)

s