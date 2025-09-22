from odoo import models,fields,api

class EventC(models.Model):
    _inherit = 'event.event'
   

    
    test = fields.Char(string='Test field')
    Sund= fields.Many2many("tags",string="Sound equipment")
    Projection= fields.Many2many("tagp",string="Projection equipment")
    organization=fields.Many2many('tagm', string='Organization')
    
    

    @api.model_create_multi
    def create(self,vals):
        res=super(EventC,self).create(vals)
        print("HE CREATE NEW EVENT")
        return res
    
    @api.model
    def write(self,vals):
        res=super(EventC,self).write(vals)
        print("HE WRITE IN EVENT")
        return res
    def unlink(self):
        res=super(EventC,self).unlink()
        print("HE DELET EVENT")
        return res

    
