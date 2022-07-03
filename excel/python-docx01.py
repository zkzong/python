from docx import Document
document = Document()
document.add_paragraph('Hello,Word!')
document.save('demo.docx')