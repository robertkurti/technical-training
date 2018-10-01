# -*- coding: utf-8 -*-
from odoo import models, fields, api, exceptions, _

class Rentals(models.Model):
    _name = 'library.rental'
    _description = 'Book rental'

    customer_id = fields.Many2one('library.partner', string='Customer')
    book_id = fields.Many2one('library.book', string='Book')
    rental_date = fields.Date(string='Rental date')
    return_date = fields.Date(string='Return date')
    name_cus = fields.Char(string='Customer Name', related='customer_id.name')
    name_cus = fields.Char(string='Address', related='customer_id.email')
    name_book = fields.Char(string='Book Name', related='book_id.name')
    name_book = fields.Char(string='ISBN', related='book_id.isbn')
    
