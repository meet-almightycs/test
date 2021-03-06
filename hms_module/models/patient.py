 #-*- coding: utf-8 -*-

from odoo import models, fields, api,_

class Hmspatient(models.Model):
    _name = 'hms.patient'

    _description = "hmsPatient"

    def appintment_count(self):
        for record in self:
            
            Count=self.env['hms.appointment'].search_count([('patient', '=', record.id)])
            print  ("mmmmmmmmmmmmmmmmmmmmmmmmmmm",Count)
            record.appointment_count=Count
        # self.search_count([('patient', '=', )])

    name = fields.Char(string = "Name" ,required = True)
    identification_code= fields.Char(string='Identification Code', required=True, translate=True)
    gender = fields.Selection([
            ('male', 'Male'),
            ('female', 'Female'),
            ], required=True,string='Gendar')
    date_of_birth = fields.Date (string = 'Date of Birth' , required = True)
    age = fields.Char (string = 'Age' , required= True)
    address = fields.Char(string = 'Address' , required = True)
    occupation_patient_education_religion_tribe_ethnic_group = fields.Char(string= 'Occupation Patient Education Religion Tribe Ethnic group' ,required = True)
    phone = fields.Char(string='Phone' , required=True)
    mobile_no = fields.Char(string = 'Mobile No.' , required = True)
    email = fields.Char(string = 'Email' , required= True)
    blood_group = fields.Selection([
     				('AB+','AB+'),
     				('AB-','AB-'),
     				('O+','O+'),
     				('O-','O-'),
     	            ], required = True , string = 'Blood Group')
    is_blood_receiver = fields.Boolean (string  ='Is Blood Receiver')
    is_blood_donor = fields.Boolean	(string = 'Is Blood Donor' , required = True)
    is_child = fields.Boolean (string = 'Is Child' , required = True)
    family = fields.Char(string='family')
    #name = fields.Char(string='Patient', translate=True, required= True)
    doctor = fields.Selection([
             ('MBBS','MBBS'),
             ('MD','MD'),
             ], string='Digree')
    medical_alert = fields.Many2many('madical.alert' , string='Madical Alert')
    appointment_count = fields.Integer(compute='appintment_count', string='Appointment Count')



class hmsPatientmadicalalert(models.Model):         
   _name = 'madical.alert'
   _description = "madical alert"

   specialty = fields.Char(string="Specialty", required = True , translate = True)
   name = fields.Char(string="Name")

