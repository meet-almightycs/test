 #-*- coding: utf-8 -*-

from odoo import models, fields, api,_ 



class Hmsappointment(models.Model):
    _name = 'hms.appointment'
    _description = "hmsappointment"
    
    identification_no = fields.Char(string='Identification No' ,required = True)
    patient = fields.Many2one('hms.patient' , string = "Patient" , required=True)
    age = fields.Char(string = 'Age' , required = True)
    physician = fields.Many2one('hms.doctor' , string = "Physician")
    date = fields.Datetime (string = 'Date' , required = True)
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

