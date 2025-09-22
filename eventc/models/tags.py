from odoo import models,fields

class Equipment(models.Model):
    _name="tags"
    _description="equipment object"
    _res_name="name"
    
    name = fields.Char(string="Sound equipment", required=True)
    color = fields.Integer(string='Color')
