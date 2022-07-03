import PyPDF2

pdff1 = open("123.pdf", "rb")
pr = PyPDF2.PdfFileReader(pdff1)
print(pr.numPages)

pdff2 = open("456.pdf", "rb")
pr2 = PyPDF2.PdfFileReader(pdff2)

pdf3 = open("789.pdf", "rb")
pr3 = PyPDF2.PdfFileReader(pdf3)

pdfw = PyPDF2.PdfFileWriter()
pageobj = pr.getPage(0)
pdfw.addPage(pageobj)

for pageNum in range(pr2.numPages):
    pageobj2 = pr2.getPage(pageNum)
    pdfw.addPage(pageobj2)

pageobj3 = pr3.getPage(0)
pdfw.addPage(pageobj3)

pdfout = open("aaa.pdf", "wb")
pdfw.write(pdfout)
pdfout.close()
pdff1.close()
pdff2.close()
pdf3.close()
