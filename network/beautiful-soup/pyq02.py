from pyquery import PyQuery as pyq

html = '''
<html>
    <title>这是标题</title>
<body>
    <p id="hi">Hello</p>
    <ul>
        <li>list1</li>
        <li>list2</li>
    </ul>
</body>
</html>
'''
jq = pyq(html)
print(jq('title'))  # 获取 title 标签的源码
print(jq('title').text())  # 获取 title 标签的内容
print(jq('#hi').text())  # 获取 id 为 hi 的标签的内容

li = jq('li')  # 处理多个元素
for i in li:
    print(pyq(i).text())

