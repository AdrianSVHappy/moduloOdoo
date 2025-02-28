from odoo import models, fields, api

"""
Experimentos -> titulo, campo, investigadores, materiales
"""

class lab_experimento(models.Model):
    #Informacion
    _name = 'lab.experimento'
    _description = 'Experimento'
    
    #Campos
    name = fields.Char(string="Titulo", required=True)
    campo = fields.Selection([('1','Biologia'),('2','Fisica'),('3','Quimica')], required=True)
    
    
    #Relaciones
    investigadores = fields.One2many('lab.investigador', 'experimento')
    materiales = fields.Many2many('lab.material')
    
    #Calculados
    progresion = fields.Integer(default=0, inverse="_progreso")
    realizada = fields.Boolean(readonly=True, compute="_progreso")

    @api.depends('progresion', 'realizada')      
    def _progreso(self):
        for x in self:
            if x.progresion > 100:
                x.progresion = 100
            elif x.progresion < 0:
                x.progresion = 0
            
            if x.progresion == 100:
                x.realizada = True
            else:
                x.realizada = False

