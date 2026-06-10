from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph
)

from reportlab.lib.styles import getSampleStyleSheet

class PDFExporter:

    def export(self, filename, report):

        doc = SimpleDocTemplate(filename)

        styles = getSampleStyleSheet()

        elements = [
            Paragraph(report, styles['BodyText'])
        ]

        doc.build(elements)
