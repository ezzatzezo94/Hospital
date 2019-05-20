from odoo import models, fields, api


class reveal(models.Model):
    _name = 'hospital.reveal'
    _rec_name = 'code'

    code = fields.Char()
    description = fields.Text(string="Description", required=False, )
    sections_ids = fields.Many2many(comodel_name="hospital.sections", string="Department", required=False, )
    patient_id = fields.Many2one(comodel_name="res.partner", domain="[('function','=','patient')]", string="Patient",
                                 required=False, )
    doctor_id = fields.Many2many(comodel_name="res.partner", domain="[('function','=','doctor'),('sections_id','=',"
                                                                   "sections_ids)]", string="Doctor", required=False, )

    '''override create method'''

    @api.model
    def create(self, vals):
        vals['code'] = self.env['ir.sequence'].next_by_code('hospital.reveal')
        res = super(reveal, self).create(vals)

        return res
