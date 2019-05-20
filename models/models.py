# -*- coding: utf-8 -*-

from odoo import models, fields, api


class partner(models.Model):
    _name = 'res.partner'
    _inherit = 'res.partner'
    _rec_name = 'name'

    sections_id = fields.Many2one(comodel_name="hospital.sections", string="Department", required=False, )
    function = fields.Selection(selection=[('doctor', 'Doctor'), ('patient', 'Patient'), ('nurse', 'Nurse')],
                                required=False, )
