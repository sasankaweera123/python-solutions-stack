from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font('Helvetica', 'B', 12)
        self.cell(0, 10, 'Report', 0, 1, 'C')

    def chapter_title(self, title):
        self.set_font('Helvetica', 'B', 12)
        self.cell(0, 10, title, 0, 1, 'L')
        self.ln(10)

    def chapter_body(self, body):
        self.set_font('Helvetica', '', 12)
        self.multi_cell(0, 10, body)
        self.ln()

    def add_table(self, table_data, col_widths=None):
        if col_widths is None:
            col_widths = [40, 50, 50]

        row_height = 10
        self.set_font('Helvetica', '', 12)

        for row in table_data:
            for i, datum in enumerate(row):
                self.cell(col_widths[i], row_height, datum, border=1)
            self.ln(row_height)

pdf = PDF()
pdf.add_page()

# Table data
table_data = [
    ('Etap', 'Czas rozpoczecia', 'Czas trwania'),
    ('Wychladzanie pieca', 'IDLE_start', ''),
    ('NIF temp = 1200C', 'IDLE_step1', 'IDLE_time_step1'),
    ('Przycisk DROP', 'IDLE_step2', 'IDLE_time_step2'),
    ('DROP', 'IDLE_step3', 'IDLE_time_step3'),
    ('Preciki - START', 'IDLE_step4', 'IDLE_time_step4'),
    ('Preciki - STOP', 'IDLE_step5', 'IDLE_time_step5'),
    ('V = 15 m/min', 'IDLE_step6', 'IDLE_time_step6'),
    ('V = 50 m/min', 'IDLE_step7', 'IDLE_time_step7'),
    ('Srednica w tolerancji', 'IDLE_step8', 'IDLE_time_good'),
    ('Predkosc robocza', 'IDLE_end', 'IDLE_time_end')
]

pdf.set_font('Helvetica', 'B', 18)
pdf.cell(0, 10, 'Table', 0, 1, 'C')
pdf.ln(10)

pdf.add_table(table_data)

pdf.output('table.pdf')
