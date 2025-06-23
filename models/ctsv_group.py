from odoo import models, fields

class CTSVGroup(models.Model):
    _name = 'ctsv.group'
    _description = 'Nhóm CTSV chăm sóc sinh viên'

    name = fields.Char('Tên nhóm', required=True)
    member_ids = fields.Many2many('res.users', string='Thành viên')