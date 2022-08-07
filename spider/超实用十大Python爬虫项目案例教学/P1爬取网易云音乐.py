# author: admin
# date: 2022/8/7 14:11

"""
爬取网易云音乐热歌榜歌曲
"""
import os
import re

import requests

filename = "music/"
if not os.path.exists(filename):
    os.mkdir(filename)

# 如果想要爬取其他的榜单的歌曲内容，只需要更改请求url中的ID
url = 'https://music.163.com/discover/toplist?id=3778678'

# headers请求头就是用来伪装python代码的，把python代码伪装成浏览器对于服务器发送请求
# 服务器接收到请求之后，会给我们返回响应数据（response）
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'
}
response = requests.get(url=url, headers=headers)
# print(response.text)
html_data = re.findall('<li><a href="/song\?id=(\d+)">(.*?)</a>', response.text)
# 正则表达式提取出来的一个内容，返回是列表，里面每一个元素都是元组
for num_id, title in html_data:
    music_url = 'https://music.163.com/song/media/outer/url?id={}.mp3'.format(num_id)
    # 对于音乐播放地址发送请求，获取二进制数据内容
    music_content = requests.get(music_url, headers=headers).content
    with open(filename + title + '.mp3', mode='wb') as file:
        file.write(music_content)
    print(num_id, title)
