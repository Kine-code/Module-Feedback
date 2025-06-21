# -*- coding: utf-8 -*-
from odoo import models, fields, api


class SurveyFeedback(models.Model):
    _name = 'survey.feedback'
    _description = 'Phản hồi khách hàng tại quầy'
    _order = 'submitted_at desc'

    feedback = fields.Selection([
        ('good', 'Tốt 😊'),
        ('fair', 'Khá 🙂'),
        ('average', 'Trung bình 😐'),
        ('bad', 'Kém 😞'),
    ], string='Mức đánh giá', required=True)

    submitted_at = fields.Datetime(
        string='Thời gian phản hồi',
        default=fields.Datetime.now,
        readonly=True
    )

    kiosk_group_id = fields.Many2one('survey.feedback.group', string='Quầy phản hồi')

    count = fields.Integer(string='Count', default=1, store=True)

    @api.model
    def create(self, vals):
        vals['count'] = 1
        return super(SurveyFeedback, self).create(vals)
    
    def name_get(self):
        """Tùy chỉnh tên hiển thị trong tree view"""
        result = []
        for record in self:
            label = f"[{record.submitted_at.strftime('%Y-%m-%d %H:%M')}] - {dict(self._fields['feedback'].selection).get(record.feedback)}"
            result.append((record.id, label))
        return result
