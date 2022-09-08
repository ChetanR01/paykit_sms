from odoo import models,fields,api
# from odoo.addons.prisms_sms.models.sms_server import send_prisms_sms
# for sms
import urllib.parse
from urllib.request import Request, urlopen

class SMSTemplate(models.Model):
    _name = "prisms_sms.template"
    # Template related stuff
    name = fields.Char(string="Template Name")
    description = fields.Char(string="Description")
    template = fields.Text(string="Template")
    route = fields.Integer(string="Route")
    # server related stuff
    template_id = fields.Char(string="DLT_TE_ID")
    authkey = fields.Char(string="authkey")
    sender = fields.Char(string="Sender")

    @api.depends('template')
    def send_short_msg(self,ex_msg):
        print("### THIS IS SHORT MSG")
        print("### template>> \n",self.template)
        print("### \n external msg is>> ",ex_msg)




# send_prisms_sms(internal_template_id,phone_no,name,points_earned,create_date,points)
def send_prisms_sms(phone_no,name,points_earned,create_date,points):
    # template_obj =self.env["prisms_sms.template"].search['id','=',internal_id]
    # for word in raw_template:
    #     if word =="{#var#}":
    #         pass
    # raw_template = template_obj.template # 

    
    authkey = "177166AsuwEp1r630325e1P1"
    mobiles = phone_no
    message = f"""Dear {name}, You have earned points worth {points_earned} for your transaction on date {create_date} Your current points balance is {points} -SANGAM """

    sender = "HSANGM"
    route = "4"
    values = {
                    'authkey' : authkey,
                    'mobiles' : mobiles,
                    'message' : message,
                    'sender' : sender,
                    'route' : route,
                    'DLT_TE_ID': '1207165833594730331'
                    }
    url = "http://sms.prisms.in/api/sendhttp.php" # API URL
    data = urllib.parse.urlencode(values)
    data= data.encode("utf-8")
    req = urllib.request.Request(url, data, headers={'User-Agent': 'Mozilla/5.0'})
    response = urllib.request.urlopen(req)
    output = response.read() # Get Response
    print("####Output>>>",output)




# print("##### the function is working! if ",testvar)    
pass



    
    