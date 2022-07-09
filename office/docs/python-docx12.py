from docx import Document
from docx.shared import Pt
from docx.enum.style import WD_STYLE_TYPE

doc = Document()
for i in range(10):
    p = doc.add_paragraph(u'段落 %d' % i)
    style = doc.styles.add_style('UserStyle%d' % i, WD_STYLE_TYPE.PARAGRAPH)
    style.font.size = Pt(i + 20)
    p.style = style

doc.save('../file/third/style-1.docx')
