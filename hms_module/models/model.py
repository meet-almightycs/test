# -*- coding: utf-8 -*-

from odoo import models, fields, api,_ 



class Hmsdoctor(models.Model):
    _name = 'hms.doctor'

    _description = "hmsDoctor"

    name = fields.Char(string='Doctor', required=True, translate=True)
    doctor_id = fields.Char(string = 'Doctor Id' , required = True)
    primary_surgeon = fields.Boolean(string = 'Primary Surgeon')
    consultation_physician = fields.Boolean(string = 'Consultation Physician')
    government_id = fields.Char(string = 'Government ID' , required = True)
    specialty = fields.Many2one('specialty' , string = "Specialty")
    photo = fields.Image("Photo", max_width=1920, max_height=1920)
    mobile_No = fields.Char(string= ' Mobile No.' , required = True)
    address = fields.Char(string = 'Address' , required = True)
    allowed_online_booking = fields.Boolean(string = 'Allowed Online Booking')
    amount = fields.Float (string = 'Amount')
    family = fields.One2many('hms.patient', 'family', 'family')
    doctor_type= fields.Selection([
            ('male', 'Male'),
            ('female', 'Female'),
        ], required=True,string='Gendar')
    note = fields.Text(string='prescription', translate=True) 
    doctor_name_id = fields.Many2one('hms.patient', string='Patient')

    reconciled_invoice_ids = fields.Many2many('account.move', string='Reconciled Invoices', compute='_compute_reconciled_invoice_ids', help="Invoices whose journal items have been reconciled with these payments.")
    has_invoices = fields.Boolean(compute="_compute_reconciled_invoice_ids", help="Technical field used for usability purposes")
   # move_line_ids = fields.One2many('account.move.line', 'payment_id', readonly=True, copy=False, ondelete='restrict')
   




class hmspatient(models.Model):
    _name = 'hms.patient'
    _description = "Patient"
    
    name = fields.Char(string='Patient', required=True, translate=True)
    doctor = fields.Selection([
            ('MBBS', 'MBBS'),
            ('MD', 'M_D'),

            ], required=True, string='Digree')
     
    family = fields.Char(string='family' , required = True)





class specialty(models.Model):         
   _name = 'specialty'
   _description = "specialty"

   specialty = fields.Char(string="Specialty", required = True , translate = True)
