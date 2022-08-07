# author: admin
# date: 2022/8/7 16:17

'''
采集4K超清壁纸
'''
import re

import requests

for page in range(1,11):
    url = f'https://wallhaven.cc/search?q=4k&categories=111&purity=100&sorting=relevance&order=desc&page={page}'
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
    }
    res = requests.get(url=url, headers=header)
    print(res.text)
    href = re.findall('<a class="preview" href="(.*?)"', res.text)
    print(href)
    for link in href:
        html_data = requests.get(url=link, headers=header).text
        print(html_data)
        img_info = re.findall('<img id="wallpaper" src="(.*?)" alt="(.*?)"', html_data)
        img_content = requests.get(url=img_info[0][0], headers=header).content
        with open('img/' + img_info[0][1] + '.jpg', mode='wb') as file:
            file.write(img_content)
