# 引入所需要的基本包
from reportlab.pdfgen import canvas


# 设置绘画开始的位置
def hello(c):
    c.drawString(100, 100, "hello world!")


# 定义要生成的pdf的名称
c = canvas.Canvas("1.pdf")
# 调用函数进行绘画，并将canvas对象作为参数传递
hello(c)
# showPage函数：保存当前页的canvas
c.showPage()
# save函数：保存文件并关闭canvas
c.save()
