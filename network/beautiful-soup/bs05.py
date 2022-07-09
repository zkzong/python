html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""
from bs4 import BeautifulSoup

soup = BeautifulSoup(html, 'lxml')
title_tag = soup.title
print(title_tag)
print(title_tag.parent)
# 在下面代码中，因为<b>标签和<c>标签是同一层:他们是同一个元素的子节点,
# 所以<b>和<c>可以被称为兄弟节点.一段文档以标准格式输出时,
# 兄弟节点有相同的缩进级别.在代码中也可以使用这种关系.
sibling_soup = BeautifulSoup("<a><b>text1</b><c>text2</c></b></a>", 'lxml')
print(sibling_soup.prettify())
# <b>标签有 .next_sibling 属性,但是没有 .previous_sibling 属性,因为<b>标签在同级节点中是第一个
# 同理,<c>标签有 .previous_sibling 属性,却没有 .next_sibling 属性
print(sibling_soup.b.next_sibling)
print(sibling_soup.c.previous_sibling)

for sibling in soup.a.next_siblings:
    print(repr(sibling))

for sibling in soup.find(id="link3").previous_siblings:
    print(repr(sibling))
