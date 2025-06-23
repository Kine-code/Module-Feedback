from odoo import models, fields

class CTSVStudent(models.Model):
    _name = 'ctsv.student'
    _description = 'Thông tin Sinh viên'

    name = fields.Char('Họ tên', required=True)
    student_code = fields.Char('Mã số sinh viên', required=True)
    class_name = fields.Char('Lớp')
    group_id = fields.Many2one('ctsv.group', string='Nhóm CTSV phụ trách')