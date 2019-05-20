from odoo import models, fields, api

class room(models.Model):
    _name = 'hospital.room'
    _rec_name = 'room_code'

    room_code = fields.Char( )
    devices_ids = fields.Many2many(comodel_name="hospital.device",string="devices", )

    '''override create method'''
    @api.model
    def create(self, vals):
        vals['room_code'] = self.env['ir.sequence'].next_by_code('hospital.room')
        new_record = super(room, self).create(vals)

        return new_record





class device(models.Model):
    _name = 'hospital.device'
    _rec_name = 'name'



    name = fields.Char(string="Name", required=True, )
    code = fields.Char()
    quantity = fields.Integer(string="Quantity", required=False, )

    '''override create method'''
    @api.model
    def create(self,vals):
        vals['code'] = self.env['ir.sequence'].next_by_code('hospital.device')
        new_record = super(device, self).create(vals)

        return new_record

