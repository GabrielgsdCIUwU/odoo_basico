# -*- coding: utf-8 -*-

from odoo import models, fields, api


class suceso(models.Model):
    _name = 'odoo_basico.suceso'
    _description = 'Modelo con vista en modo tree(list)'

    name = fields.Char(required=True, size=20, string="Suceso")
    descripcion = fields.Text(string="La descripción del Suceso")
    nivel = fields.Selection([('low', 'Bajo'), ('medium', 'Medio'), ('high', 'Alto')], string='Nivel')
    fecha_hora = fields.Datetime(string="Fecha y hora", default=lambda self: fields.Datetime.now())