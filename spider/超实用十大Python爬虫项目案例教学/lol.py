"""
课程内容: python爬取英雄联盟资料库所有英雄皮肤图片包含炫彩

(今天的课程内容非常简单,零基础入门的同学也是可以掌握学习的哟)

授课老师: 青灯教育-自游

开发环境以及模块的使用:
    python 3.6
    pycharm

    requests >>> pip install requests
    os 内置模块 不需要安装的


"""
import pprint

import requests
import os
url = 'https://game.gtimg.cn/images/lol/act/img/js/heroList/hero_list.js'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'
}

def save(hero_name, name, img_url):
    filename = f'{hero_name}\\'
    if not os.path.exists(filename):
        os.mkdir(filename)
    img_content = requests.get(url=img_url).content
    with open(filename + name + '.jpg', mode='wb') as f:
        f.write(img_content)
        print(name)



response = requests.get(url=url, headers=headers)
heroes = response.json()['hero']
for hero in heroes:
    hero_id = hero['heroId']

    hero_url = f'https://game.gtimg.cn/images/lol/act/img/js/hero/{hero_id}.js'
    response_1 = requests.get(url=hero_url, headers=headers)
    skins = response_1.json()['skins']
    for index in skins:
        title = index['heroTitle']  # 安妮
        hero_name = index['heroName'] + title # 绰号 称号 黑暗之女
        img_name = index['name'] # 皮肤名字
        img_url = index['mainImg'] # 皮肤图片url
        if img_url:
            save(hero_name, img_name, img_url)
        else:
            img_url = index['chromaImg']
            save(hero_name, img_name, img_url)



















