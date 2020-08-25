 #-*- coding: utf-8 -*-

from odoo import models, fields, api,_ 



class Hmspatient(models.Model):
    _name = 'hms.patient'

    _description = "hmsPatient"

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
             ('MBBS', 'MBBS'),
             ('MD', 'M_D'),

             ], string='Digree')