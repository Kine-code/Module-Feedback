odoo.define('survey_feedback.submit', function (require) {
    'use strict';

    const publicWidget = require('web.public.widget');

    publicWidget.registry.SurveyFeedback = publicWidget.Widget.extend({
        selector: '#feedback-container',
        events: {
            'click .feedback-button': '_onFeedbackClick',
        },

        _onFeedbackClick: function (ev) {
            const self = this;
            const feedback = ev.currentTarget.dataset.feedback;
            const kioskLocation = document.getElementById('kiosk-location')?.value || '';

            // Disable all buttons to prevent double click
            this.$el.find('.feedback-button').prop('disabled', true);

            this._rpc({
                route: '/survey_feedback/submit',
                params: {
                    feedback: feedback,
                    kiosk_location: kioskLocation,
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
