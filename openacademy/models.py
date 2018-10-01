# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Courses(models.Model):
    _name = 'openacademy.course'

    name = fields.Char()
    user_id = fields.Many2one('res.users', string="Responsible")


class Sessions(models.Model):
    _name = 'openacademy.session'

    course_id = fields.Many2one('openacademy.course', string="Course")
    user_id = fields.Many2one('res.users', string="Instructor")
    start_date = fields.Date()
    seats = fields.Integer('Room Capacity')
    attendee_ids = fields.Many2many('res.partner', string="Attendees")
    number_of_atendees = fields.Integer(compute='_nbAtendees')
    
    @api.depends('attendee_ids', 'seats')
    def _nbAtendees(self):
        for record in self:
            record.number_of_atendees = len(record.attendee_ids)
            
            
    @api.onchange('attendee_ids', 'seats')
    def _onchange(self):
        if len(self.attendee_ids) > self.seats:
            raise ValidationError("Can't do That")
    

            
    @api.constrains('attendee_ids', 'seats')
    def _check(self):
        if len(self.attendee_ids) > self.seats:
            raise ValidationError("To many")
