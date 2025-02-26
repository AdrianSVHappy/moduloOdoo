from odoo import models, fields, api

"""
Informes -> investigador, experimento, materiales, texto 
"""

class lab_informe(models.Model):
    _name = 'lab.informe'
    _description = 'Informe'
    
    #Campos
    name = fields.Char(string="ID", select=True)

    
    #Relaciones
    redactor = fields.Many2one('lab.investigador')
    experimento = fields.Many2one('lab.experimento')
    
    #Calculado
    texto = fields.Text(inverse="_autoText")
#    texto = fields.Text()
    
    @api.constrains(redactor, experimento)
    def _autoText(self):
        if self.experimento and self.redactor:
            self.texto = f"Informe del experimento {self.experimento.name}.\nRedactado por {self.redactor.name} {self.redactor.apellidos}\n"