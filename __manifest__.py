{
    'name': 'survey_feedback',
    'version': '1.0',
    'summary': 'Thu thập phản hồi tư vấn tại quầy (4 mức đánh giá, không cần đăng nhập)',
    'description': """
        Thu thập phản hồi tại quầy bằng giao diện cảm ứng đơn giản: Tốt, Khá, Trung bình, Kém.
        Hiển thị cảm ơn 2 giây và tự động reset. Có thống kê theo ngày, quầy và báo cáo PDF.
    """,
    'author': 'Công Kiên',
    'website': '',
    'category': 'Feedback',
    'depends': ['base', 'web', 'website'],
    'data': [
        'security/ir.model.access.csv',
        'security/survey_feedback_security.xml',

        'views/survey_feedback_views.xml',
        'views/survey_feedback_template.xml',
        'views/survey_feedback_search.xml',

        'report/report_feedback_pdf_template.xml',
        'report/report_survey_feedback.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            'survey_feedback/static/src/js/feedback_submit.js',
        ],
    },
    'images': [
        'static/description/icon.png',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
