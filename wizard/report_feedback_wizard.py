from odoo import models, fields
from odoo.http import request
import base64
import io
import csv
from datetime import datetime


class ReportFeedbackWizard(models.TransientModel):
    _name = 'report.feedback.wizard'
    _description = 'In hoặc xuất phản hồi theo khoảng ngày'

    date_from = fields.Date(string='Từ ngày', required=True)
    date_to = fields.Date(string='Đến ngày', required=True)
    kiosk_location = fields.Char(string='Quầy (tuỳ chọn)')

    def _get_filtered_feedbacks(self):
        domain = [('submitted_at', '>=', self.date_from), ('submitted_at', '<=', self.date_to)]
        if self.kiosk_location:
            domain.append(('kiosk_location', '=', self.kiosk_location))
        return self.env['survey.feedback'].search(domain)

    def print_report(self):
        return self.env.ref('survey_feedback.action_report_survey_feedback').report_action(
            self._get_filtered_feedbacks()
        )

    def export_csv(self):
        feedbacks = self._get_filtered_feedbacks()
        csv_buffer = io.StringIO()
        writer = csv.writer(csv_buffer)
        writer.writerow(['Thời gian', 'Phản hồi', 'Quầy'])

        for rec in feedbacks:
            writer.writerow([
                fields.Datetime.to_string(rec.submitted_at),
                dict(rec._fields['feedback'].selection).get(rec.feedback),
                rec.kiosk_location or ''
            ])

        csv_data = csv_buffer.getvalue()
        csv_buffer.close()

        export_name = f"feedbacks_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
        encoded_csv = base64.b64encode(csv_data.encode('utf-8'))

        export = self.env['ir.attachment'].create({
            'name': export_name,
            'type': 'binary',
            'datas': encoded_csv,
            'res_model': self._name,
            'res_id': self.id,
            'mimetype': 'text/csv',
        })

        return {
            'type': 'ir.actions.act_url',
            'url': f'/web/content/{export.id}?download=true',
            'target': 'self',
        }
