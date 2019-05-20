from odoo import models, fields, api


class sections(models.Model):
    _name = 'hospital.sections'
    _rec_name = 'name'

    code = fields.Char()
    name = fields.Char(string='Name')



    '''override create method'''
    @api.model
    def create(self, vals):
        vals['code'] = self.env['ir.sequence'].next_by_code('hospital.sections')
        new_record = super(sections, self).create(vals)

        return new_record
