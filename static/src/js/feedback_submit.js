odoo.define('survey_feedback.submit', function (require) {
    'use strict';

    const publicWidget = require('web.public.widget');

    publicWidget.registry.SurveyFeedback = publicWidget.Widget.extend({
        selector: '#feedback-container',
        events: {
            'click #start-feedback': '_onStartFeedback',
            'click .feedback-button': '_onFeedbackClick',
        },

        _onStartFeedback: function (ev) {
            // Kiểm tra dữ liệu nhập thông tin sinh viên
            const name = document.getElementById('student-name').value.trim();
            const code = document.getElementById('student-code').value.trim();
            const className = document.getElementById('class-name').value.trim();
            const groupId = document.getElementById('ctsv-group').value;

            if (!name || !code || !groupId) {
                alert('Vui lòng nhập đầy đủ Họ tên, Mã SV và chọn Nhóm CTSV');
                return;
            }

            // Lưu vào local/session để dùng khi submit feedback
            sessionStorage.setItem('student_name', name);
            sessionStorage.setItem('student_code', code);
            sessionStorage.setItem('class_name', className);
            sessionStorage.setItem('ctsv_group_id', groupId);

            document.getElementById('student-info-form').classList.add('d-none');
            document.getElementById('feedback-form').classList.remove('d-none');
        },

        _onFeedbackClick: function (ev) {
            const self = this;
            const feedback = ev.currentTarget.dataset.feedback;
            // Lấy thông tin sinh viên từ sessionStorage
            const studentName = sessionStorage.getItem('student_name');
            const studentCode = sessionStorage.getItem('student_code');
            const className = sessionStorage.getItem('class_name');
            const groupId = sessionStorage.getItem('ctsv_group_id');

            // Disable all buttons to prevent double click
            this.$el.find('.feedback-button').prop('disabled', true);

            this._rpc({
                route: '/survey_feedback/submit',
                params: {
                    feedback: feedback,
                    student_name: studentName,
                    student_code: studentCode,
                    class_name: className,
                    ctsv_group_id: groupId,
                },
            }).then(function (result) {
                if (result.status === 'ok') {
                    self.$el.find('.row').hide();
                    self.$el.find('#thank-you-message').removeClass('d-none');
                    setTimeout(function () {
                        window.location.reload();
                    }, 2000);
                }
            });
        },
    });

    return publicWidget.registry.SurveyFeedback;
});