from markupsafe import Markup, escape
#实现支持HTML字符串的Unicode子类
print(escape("<script>alert(document.cookie);</script>"))
tmpl = Markup("<em>%s</em>")
print(tmpl % "Peter > Lustig")

#可以通过重写__html__功能自定义等效HTML标记
class Foo(object):
  def __html__(self):
   return '<strong>Nice</strong>'

print(escape(Foo()))
print(Markup(Foo()))
