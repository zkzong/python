from docx import Document
from docx.enum.style import WD_STYLE_TYPE

doc = Document()
styles = doc.styles
print("\n".join([s.name for s in styles if s.type == WD_STYLE_TYPE.PARAGRAPH]))
