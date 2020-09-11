 #-*- coding: utf-8 -*-

from odoo import models, fields, api,_ 
from datetime import date



class Hmsappointment(models.Model):
    _name = 'hms.appointment' 
    _description = "hmsappointment"

    name = fields.Char(string='Appointment No.' )
    identification_no = fields.Char(string='Identification No' ,required = True)
    patient = fields.Many2one('hms.patient' , string = "Patient" , required=True)
    age = fields.Char(string = 'Age' , required = True)
    physician = fields.Many2one('hms.doctor' , string = "Physician")
    date = fields.Datetime(string = 'Date')
    urgency_level = fields.Selection([
                    ('normal','Normal'),
                    ('urgent','Urgent'),
                    ('medical emergency','Medical Emergency'),
                    ], required = True , string = 'Urgency Level')
    purpose = fields.Char(string = 'Purpose')
    cabin = fields.Char(string = 'Cabin')
    chief_complaints = fields.Text(string = 'chief Complaints')
    responsible_jr_doctor = fields.Many2one('hms.doctor',string = 'Responsible jr. Doctor')
    history_of_present_illness = fields.Text(string = 'History Of Present Illness')
    outside_appointment = fields.Boolean (string = 'Outside Appointment')
    state = fields.Selection([
            ('draft','Quotation'),
            ('waiting','Quotation Send'),
            ('confirm','Sales Order'),
            ('conformd','Conformd'),
            ('reject','Reject'),
        ], string = 'State', default = 'draft')
    ammount = fields.Float(string = 'Ammount')
    signature = fields.Binary(string='Signature') 
    reject = fields.Text(string = 'Reject')
    @api.model
    def create(self, vals):
        #date = vals.get('date', '')
        # if tag_name:
        today = fields.Datetime.now()
       #today = date.today()
        print("Today's date------------------------------:", today)
        vals['date'] = today

        #print ("meet-----------------------:-",vals)
        # if vals.get('name'):
        #     print ("aaaa_______________________",vals)
        vals['name'] = self.env['ir.sequence'].next_by_code('hms.appointment') or 'New'
        record = super(Hmsappointment, self).create(vals)
        return record

   # @api.model
    def write(self,vals):
        print(vals)
        if 'physician' in vals:
            if vals.get('physician'):
                 purpose = "fkjweugfiycg"
                 print("uhsdic",purpose)
            else :
                purpose = ""
                print("uhsdic",purpose)
        purpose = ""
        vals['purpose'] = purpose
        record = super(Hmsappointment,self).write(vals)
        return record



    @api.onchange('patient')
    def onchange_user_id(self):
        if self.patient:
            self.age = self.patient.age

    def conform_record_name(self):
        # print("meet-----------------------:-",conformd)

        self.state = "conformd" 

    # def reject(self):
    #     self.reason = "reject" 
