from docx import Document
path = "../file/third/demo.docx"
document = Document(path)
for paragraph in document.paragraphs:
    print(paragraph.text)