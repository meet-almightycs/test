# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from odoo.exceptions import UserError


class HmsReject(models.TransientModel):
    _name = "hms.reject"
    _description = "Hms Reject"


    reason = fields.Text(string = 'Reason')
    
    def reject(self):
        appointment = self.env['hms.appointment'].browse(self._context.get('active_ids', []))
        appointment.reject = self.reason
        appointment.state = "reject"