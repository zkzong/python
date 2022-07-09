from docx import Document

document = Document()
document.add_paragraph('Hello,Word!')
document.save('../file/third/demo.docx')
