# author: zong
# date: 2022/6/28 12:12
import requests
from bs4 import BeautifulSoup
from lxml import etree

url = 'https://www.umei.cc/meinvtupian/'
resp = requests.get(url)
resp.encoding = 'utf-8'
n = 1
# print(resp.text)
html = etree.HTML(resp.text)
a = html.xpath("/html/body/main[2]/div/ul/li/a/img/@src")
for i in a:
    b = url[:19]
    # print(b+i)
    f = open('新建文件夹/tu_%s.jpg' % n, 'wb')
    f.write(requests.get(b + i).content)
    requests.get(b + i).content  # 拿到图片 不是代码
    print('ok')
    n = n + 1
