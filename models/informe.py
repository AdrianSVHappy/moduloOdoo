from odoo import models, fields, api
from datetime import datetime

"""
Informes -> investigador, experimento, materiales, texto 
"""

class lab_informe(models.Model):
    _name = 'lab.informe'
    _description = 'Informe'
    
    #Campos


    #Relaciones
    redactor = fields.Many2one('lab.investigador',  required=True)
    experimento = fields.Many2one('lab.experimento',  required=True)
    
    #Calculado
    name = fields.Char(string="ID", select=True, compute="_setId")
    texto = fields.Text(inverse="_autoText",  required=True)

    
    @api.constrains(redactor, experimento)
    def _autoText(self):
        if self.experimento and self.redactor:
            self.texto = f"Informe del experimento {self.experimento.name}.\nRedactado por {self.redactor.name} {self.redactor.apellidos}\n"
            
    def _setId(self):
        self.name = "INF-" + str(datetime.now())