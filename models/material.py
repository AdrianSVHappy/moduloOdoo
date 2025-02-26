
from odoo import models, fields, api

"""
Materiales -> nombre, cantidad
"""

class lab_material(models.Model):
    _name = 'lab.material'
    _description = 'Material'
    
    #Campos
    name = fields.Char(string="Nombre", required=True)
    
    
    #Calculados
    cantidad = fields.Integer(inverse='_noCero')
    
    
    @api.constrains(cantidad)
    def _noCero(self):
        if self.cantidad < 0:
            self.cantidad = 0