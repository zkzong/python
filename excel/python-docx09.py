from docx import Document
from docx.shared import Inches

document = Document()
for row in range(9):
    t = document.add_table(rows=1, cols=1, style='Table Grid')
    t.autofit = False  # 很重要，必须设置！
    w = float(row) / 2.0
    t.columns[0].width = Inches(w)

document.save('table-step.docx')