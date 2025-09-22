from odoo import models,fields,api

class Equipment(models.Model):
    _name="tagp"
    _description="equipment object"
    _res_name="name"
    
    name = fields.Char(string="Projection equipment", required=True)
    color = fields.Integer(string='Color')
