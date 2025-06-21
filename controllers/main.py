from odoo import http
from odoo.http import request


class SurveyFeedbackController(http.Controller):

    @http.route('/survey_feedback', type='http', auth='public', website=True, csrf=False)
    def survey_feedback_page(self, group=None, **kwargs):
        group_record = None
        if group:
            group_record = request.env['survey.feedback.group'].sudo().search([('code', '=', group)], limit=1)
        return request.render('survey_feedback.template_feedback_form', {
            'feedback_group_id': group_record.id if group_record else '',
        })


    @http.route('/survey_feedback/submit', type='json', auth='public', csrf=False)
    def submit_feedback(self, **post):
        """Nhận và lưu phản hồi từ client"""
        feedback = post.get('feedback')
        group_id = post.get('group_id')  # ✅ lấy từ JS gửi

        if feedback in ['good', 'fair', 'average', 'bad']:
            request.env['survey.feedback'].sudo().create({
                'feedback': feedback,
                'kiosk_group_id': int(group_id) if group_id else False,  # ✅ lưu đúng field Many2one
            })
            return {'status': 'ok'}

        return {'status': 'error', 'message': 'Invalid feedback'}
