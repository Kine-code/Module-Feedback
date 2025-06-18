from odoo import http
from odoo.http import request


class SurveyFeedbackController(http.Controller):

    @http.route('/survey_feedback', type='http', auth='public', website=True, csrf=False)
    def survey_feedback_page(self, **kwargs):
        """Render giao diện chọn phản hồi"""
        return request.render('survey_feedback.template_feedback_form')

    @http.route('/survey_feedback/submit', type='json', auth='public', csrf=False)
    def submit_feedback(self, **post):
        """Nhận và lưu phản hồi từ client"""
        feedback = post.get('feedback')
        kiosk_location = post.get('kiosk_location', '')

        if feedback in ['good', 'fair', 'average', 'bad']:
            request.env['survey.feedback'].sudo().create({
                'feedback': feedback,
                'kiosk_location': kiosk_location,
            })
            return {'status': 'ok'}

        return {'status': 'error', 'message': 'Invalid feedback'}
