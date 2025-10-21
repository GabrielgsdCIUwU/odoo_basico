# -*- coding: utf-8 -*-

from odoo import models, fields, api


class informacion(models.Model):
    _name = 'odoo_basico.informacion'
    _description = 'Modelo con distintos tipos de datos'

    titulo = fields.Char(string="Titulo", size=28, required=True)
    descripcion = fields.Text(string="Descripción", required=True)
    alto_cm = fields.Integer(string="Alto en centímetros")
    largo_cm = fields.Integer(string="Largo en centímetros")
    ancho_cm = fields.Integer(string="Ancho en centímetros")
    volumen = fields.Float(string="Volume:", digits=(6,2), store=True, compute="_volumen")
    peso = fields.Float(string="Peso en Kg.s", digits=(6,2), default=2.7)
    autorizado = fields.Boolean(string="¿Autorizado?", default=False)
    sexo = fields.Selection([ ('male', 'Hombre'), ('female', 'Mujer'), ('other', 'Otro')], string="Sexo")

    @api.depends('alto_cm', 'ancho_cm', 'largo_cm')
    def _volumen(self):
        for register in self:
            register.volumen = (float(register.alto_cm) * float(register.ancho_cm) * float(register.largo_cm)) / 1000000

#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

