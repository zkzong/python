"""
[课程内容]：Python爬取笔趣阁小说

[课程时间]：14:30开始

[授课老师]：巳月老师

[知识点]：
    requests发送请求
    非结构化数据解析

[第三方库]：
    requests >>> pip install requests

[开发环境]：
    版 本： python  3.8
    编辑器：pycharm 2021.2

先听一下歌, 等一下后面进来的同学, 14:30开始讲课 有什么喜欢听的歌 也可以发在公屏上

[没听懂?]
课后的回放录播资料找木子老师微信: python10010
+python安装包 安装教程视频
+pycharm 社区版 专业版 及 激活码免费

网站分析(数据来源分析)
    1. 访问到 章节页面 https://www.bbiquge.net/book_88109/
    2. 获取所有章节链接
    3. 访问所有章节链接 拿到所有小说数据 进行保存操作
代码实现
    1. 发送请求
    2. 获取数据
    3. 解析数据
    4. 发送请求
    5. 解析数据
    6. 保存数据

系统课程: 七个月时间
从零基础开始 - 职业化课程
核心编程
爬虫开发
数据分析
网站开发
"""
import requests     # 发送请求
import parsel       # 解析数据
import re

# 伪装
headers = {
    # 浏览器的基本信息
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36'
}
url = 'https://www.bbiquge.net/book_88109/'
# 1. 发送请求
response = requests.get(url=url, headers=headers)
# 2. 获取数据
html_data = response.text
# 3. 解析数据
selector = parsel.Selector(html_data)
# ::attr(属性名): 标签属性内容
# ::text: 获取标签文本内容
link_list = selector.css('.zjlist dd a::attr(href)').getall()
title_list = selector.css('.zjlist dd a::text').getall()
zip_data = zip(title_list, link_list)
for title, link in zip_data:
    link = 'https://www.bbiquge.net/book_88109/' + link
    print(title, link)
    # 4. 发送请求
    response_1 = requests.get(link, headers=headers)
    # 5. 解析数据
    text = re.findall('<div id="content">(.*?)</div>', response_1.text)[0]
    text = text.replace(' 笔趣阁 www.bbiquge.net，最快更新<a href="https://www.bbiquge.net/book_88109/">盗墓笔记 (全本)</a>最新章节！<br><br>', '')
    text = text.replace('<br />', '\n').replace('&nbsp;', ' ')
    text = '\n'+ title + '\n' + text + '\n'
    # 6. 保存数据
    with open('盗墓笔记.txt', mode='a', encoding='utf-8') as f:
        f.write(text)
