# -*- coding: utf-8 -*-

from odoo import models, fields, api


class informacion(models.Model):
    _name = 'odoo_basico.informacion'
    _description = 'Modelo con distintos tipos de datos'

    titulo = fields.Char(string="Titulo", size=28, required=True)
    descripcion = fields.Text(string="Descripción", required=True)
    alto_cm = fields.Integer(string="Alto en centímetros")
    largo_cm = fields.Integer(string="Largo en centímetros")
    volumen = fields.Integer(string="Volumen")
    peso = fields.Integer(string="Peso en Kg.s")
    densidad = fields.Integer(string="Densidad")
    autorizado = fields.Boolean(string="¿Autorizado?", default=True)


#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

