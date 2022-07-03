#引入所需要的基本包
from reportlab.pdfgen import canvas
from reportlab.lib.units import mm

def drawBitmap(c):
    c.drawImage("123.png", 5*mm, 5*mm, 62*mm, 88.6*mm)

#定义要生成的pdf的名称
c=canvas.Canvas("4.pdf")
#调用函数生成条形码和二维码，并将canvas对象作为参数传递
drawBitmap(c)
#showPage函数：保存当前页的canvas
c.showPage()
#save函数：保存文件并关闭canvas
c.save()