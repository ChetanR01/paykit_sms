from odoo import http
from odoo.http import request
from .. import models

# for sms
import urllib.parse
from urllib.request import Request, urlopen


class PrismsSMS():
    # send_prisms_sms(internal_template_id,phone_no,name,points_earned,create_date,points)

    # def send_prisms_sms(external_temp_id,phone_no,name,points_earned,create_date,points):
    def send_prisms_sms(**sms_data):
        internal_template_id = sms_data['internal_template_id']
        template_obj = request.env['prisms_sms.template'].sudo().search([('id','=',internal_template_id)])
        
        # extract data from argument dict
        name =""
        if 'name' in sms_data:
            name=sms_data['name']
        phone_no=""
        if 'phone_no' in sms_data:
            phone_no=sms_data['phone_no']
        points_earned=""
        if 'points_earned' in sms_data:
            points_earned=sms_data['points_earned']
        create_date=""
        if 'create_date' in sms_data:
            create_date=sms_data['create_date']
        available_balance =""
        if 'available_balance' in sms_data:
            available_balance=sms_data['available_balance']
        OTP =""
        if 'OTP' in sms_data:
            OTP=sms_data['OTP']
        redeem_points =""
        if 'redeem_points' in sms_data:
            redeem_points=sms_data['redeem_points']
        PIN =""
        if 'PIN' in sms_data:
            PIN=sms_data['PIN']
        pos_name=""
        if 'pos_name' in sms_data:
            pos_name=sms_data['pos_name']
        redeem_token=""
        if 'redeem_token' in sms_data:
            redeem_token=sms_data['redeem_token']

        raw_template= template_obj.template
        
        authkey = template_obj.authkey 
        mobiles = sms_data['phone_no']
        message = raw_template.format(name=name, points_earned=points_earned, create_date=create_date, available_balance=available_balance,OTP= OTP,redeem_points= redeem_points, pos_name=pos_name, phone_no= phone_no, PIN=PIN,redeem_token=redeem_token)  

        # name, points_earned, create_date, available_balance, OTP, redeem_points, pos_name, phone_no, PIN
        # f"""Dear {name}, You have earned points worth {points_earned} for your transaction on date {create_date} Your current points balance is {points} -SANGAM """

        sender = template_obj.sender 
        route = template_obj.route 
        template_code =  template_obj.template_id
        values = {
                        'authkey' : authkey,
                        'mobiles' : mobiles,
                        'message' : message,
                        'sender' : sender,
                        'route' : route,
                        'DLT_TE_ID': template_code
                        }
        url = "http://sms.prisms.in/api/sendhttp.php" # API URL
        data = urllib.parse.urlencode(values)
        data= data.encode("utf-8")
        req = urllib.request.Request(url, data, headers={'User-Agent': 'Mozilla/5.0'})
        response = urllib.request.urlopen(req)
        output = response.read() # Get Response
        print("####Output>>>",output)


