from odoo import models, fields

"""
Investigadores -> nombre, apellidos, experimento
"""
class lab_investigador(models.Model):
    #Informacion
    _name = 'lab.investigador'
    _description = 'Investigador'
    
    #Campos
    name = fields.Char(string="nombre", required=True)
    apellidos = fields.Char()
    
    #Relaciones
    
    
