 #-*- coding: utf-8 -*-

from odoo import models, fields, api,_ 


class Hmspatientextension(models.Model):
    _inherit = 'hms.patient'

    surname = fields.Char(string = "Surname")