from odoo import models, fields

"""
Experimentos -> titulo, campo, investigadores, materiales
"""

class lab_experimento(models.Model):
    #Informacion
    _name = 'lab.experimento'
    _description = 'Experimento'
    
    #Campos
    name = fields.Char(string="Titulo", required=True)
    campo = fields.Char()
    
    
    #Relaciones
    investigadores = fields.One2many('lab.investigador', 'experimento', readonly=True)
    materiales = fields.Many2many('lab.material')