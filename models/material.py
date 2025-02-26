
from odoo import models, fields

"""
Materiales -> nombre, sin_usar, total
"""

class lab_material(models.Model):
    _name = 'lab.material'
    _description = 'Material'
    
    #Campos
    name = fields.Char(string="Nombre", required=True)
    
    
    #Calculados
    sin_usar = fields.Integer()
    total = fields.Integer()