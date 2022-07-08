from docx import Document
import sys
path = "../file/third/demo.docx"
document = Document(path)
for p in document.paragraphs:
    print(len(p.text))
    print(p.style.name)
