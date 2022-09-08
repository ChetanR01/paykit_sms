from odoo import fields,models,api

class SMSServer(models.Model):
    _name = "prisms_sms.server"

    name = fields.Char(string="Description")
    authkey = fields.Char(string="authkey")
    sender = fields.Char(string="Sender")
    
    
