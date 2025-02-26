from odoo import models, fields

"""
Informes -> investigador, experimento, materiales, texto 
"""

class lab_informe(models.Model):
    _name = 'lab.informe'
    _description = 'Informe'
    
    #Campos
    name = fields.Char(string="ID", select=True)
    texto = fields.Char()