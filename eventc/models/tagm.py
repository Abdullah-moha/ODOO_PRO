from odoo import models,fields 

class Members(models.Model):
    _name="tagm"
    _description="members object"
    _res_name="name"
    
    name=fields.Char(string='First name')
    lname=fields.Char(string='Last name')
    phone=fields.Char(string='Phone')
    email=fields.Char(string='Email')
    gender=fields.Selection([
        ('mr','Mr'),
        ('mrs','Mrs')
        ],string='Mr / Mrs')
    jdata=fields.Date(string='Joing date')
    image=fields.Binary(string='Image')
    event=fields.Many2one('event.event', string='Event orgainzer')
    re=fields.Text(string='Recommendation')
    co=fields.Text(string='Comments')
    color = fields.Integer(string='Color')