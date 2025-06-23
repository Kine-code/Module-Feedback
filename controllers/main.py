from odoo import http
from odoo.http import request

class SurveyFeedbackController(http.Controller):

    @http.route('/survey_feedback', type='http', auth='public', website=True, csrf=False)
    def survey_feedback_page(self, **kwargs):
        groups = request.env['ctsv.group'].sudo().search([])
        return request.render('survey_feedback.template_feedback_form', {'groups': groups})

    @http.route('/survey_feedback/submit', type='json', auth='public', csrf=False)
    def submit_feedback(self, **post):
        feedback = post.get('feedback')
        student_name = post.get('student_name')
        student_code = post.get('student_code')
        class_name = post.get('class_name')
        ctsv_group_id = post.get('ctsv_group_id')

        # Kiểm tra có sinh viên chưa, nếu chưa thì tạo mới
        Student = request.env['ctsv.student'].sudo()
        student = Student.search([('student_code', '=', student_code)], limit=1)
        if not student:
            student = Student.create({
                'name': student_name,
                'student_code': student_code,
                'class_name': class_name,
                'group_id': ctsv_group_id,
            })

        if feedback in ['good', 'fair', 'average', 'bad'] and student:
            request.env['survey.feedback'].sudo().create({
                'feedback': feedback,
                'student_id': student.id,
                'ctsv_group_id': ctsv_group_id,
            })
            return {'status': 'ok'}

        return {'status': 'error', 'message': 'Invalid feedback or student'}