from pyquery import PyQuery as pq
doc = pq(filename='123.html')
print(doc)
print(doc('head'))

doc1 = pq(url="http://www.baidu.com",encoding='utf-8')
print(doc1)
print(doc1('head'))