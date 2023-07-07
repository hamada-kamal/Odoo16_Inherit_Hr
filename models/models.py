from odoo import models, fields, api


class UpdateHR(models.Model):
    _inherit = "hr.employee"

    code = fields.Char(string="Employee Code")
