 #-*- coding: utf-8 -*-

from odoo import models, fields, api,_ 


class Hmsprescription(models.Model):
    _name = 'hms.prescription' 
    _description = "hmsprescription"


    patient = fields.Many2one('hms.patient' , string = 'Patient')
    prescribing_doctor = fields.Many2one('hms.doctor', string = 'Prescribing Doctor')
    medicaments_group = fields.Many2one('medicaments.group', string= 'Medicaments Group')
    disease = fields.Many2one('hms.disease', string = 'Disease')
    prescription_date = fields.Datetime (string = 'Prescription Date')
    pregnancy_warning = fields.Boolean (string = 'Pregnancy Warning')



class hmsdisease(models.Model):         
   _name = 'hms.disease'
   _description = "hmsdisease"
   
   name = fields.Char(string='Name', required = True , translate = True) 
   code = fields.Char(string='Code')
   classification = fields.Selection([
            ('ICD-9','ICD-9'),
            ('ICD-10','ICD-10'),
            ('ICD-11','ICD-11'),
        ], required=True,string='Classification')


class medicamentsgroup(models.Model):
    _name = 'medicaments.group'
    _description = "MedicamentGroup"

    name = fields.Char(string = 'Name')