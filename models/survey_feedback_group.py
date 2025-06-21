from odoo import models, fields

class SurveyFeedbackGroup(models.Model):
    _name = 'survey.feedback.group'
    _description = 'Nhóm phản hồi (quầy)'

    name = fields.Char(string='Tên quầy', required=True)
    code = fields.Char(string='Mã nhóm trên URL', required=True, index=True)
