#引入所需要的基本包
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
#设置绘画开始的位置
def hello(c):
    #设置描边色
    c.setStrokeColorRGB(0, 0, 1.0)
    #设置填充色
    c.setFillColorRGB(1,0,1)
    # draw some lines
    c.line(0.1*inch, 0.1*inch, 0.1*inch, 1.7*inch)
    c.line(0.1*inch, 0.1*inch, 1*inch, 0.1*inch)
    # draw a rectangle
    c.rect(0.2*inch, 0.2*inch, 1*inch, 1.5*inch, fill=1)
#定义要生成的pdf的名称
c=canvas.Canvas("3.pdf")
#调用函数进行绘画，并将canvas对象作为参数传递
hello(c)
#showPage函数：保存当前页的canvas
c.showPage()
#save函数：保存文件并关闭canvas
c.save()