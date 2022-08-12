"""
[课    题]： Python爬取漫客栈VIP会员漫画

[主讲老师]：青灯教育 - 自游  上课时间: 14:35

[知识点]：
    1. 爬虫基本流程
    2. parsel数据解析模块的简单使用
    3. os文件操作的简单使用
    4. 拼接图片

[开发环境]：
    Python 3.8  解释器
    Pycharm

[模块使用]:
    requests >>> pip install requests  发送请求
    parsel >>> pip install parsel      解析数据
    os  文件操作 内置模块

win + R 输入cmd 输入安装命令 pip install 模块名 如果出现爆红 可能是因为 网络连接超时 切换国内镜像源
先听一下歌 等一下后面进来的同学, 14:35正式开始讲课 [有什么喜欢听得歌曲 也可以在公屏发一下]
相对应的安装包/安装教程/激活码/使用教程/学习资料/工具插件 可以加木子老师微信: python10010

听课建议:
    1. 不要跟着敲代码, 先听思路, 课后找木子老师领取录播, 然后看视频复习写代码
    2. 如果有不懂的地方, 可以直接在公屏上面, 具体哪行代码或者那个操作不清楚..
    3. 不要早退,  早退没有录播


爬虫基本思路流程:  (固定的一个流程, 无论是采集任何网站 数据内容, 都可以按照这个流程去操作)

一. 数据来源分析 (抓包分析, 找寻数据内容)
    1. 鼠标右键点击检查/ F12, 选择network (抓包地方, 抓取数据包)  点击刷新网页
    2. 通过img过滤数据内容, 可以分析得到图片url地址
    3. 通过图片url地址, 分析找寻, 图片数据包(包含了本话所有漫画内容)  [仅仅一话的内容]
    4. 图片数据包[对比两个漫画数据包url请求参数变化规律]
    5. 只需要获取所有章节ID, 就可以获取这整本漫画的内容

获取所有章节ID >>> 把这个章节ID传入到 图片数据包里面 >>> 获取所有漫画图片url地址 >>> 保存数据

二. 代码实现的过程:
    1. 发送请求, 对于 https://www.mkzhan.com/212976/ 发送请求
    2. 获取数据, 获取服务器返回响应数据
    3. 解析数据, 提取我们想要的章节ID / 章节名字

    4. 发送请求, 对于图片数据包发送请求
    5. 获取数据, 获取服务器返回响应数据
    6. 解析数据, 提取我们想要图片url地址

    7. 保存数据

每周 三节课 每周 135或者 246 晚上20:00-22:00 周一上课学习 周二写作业复习 周三上课学习 周四写作业复习 每天3-4个小时
每节课后都是有录播回放的

最晚下班凌晨两三点下班 ,  最早 九 十点
"""
import requests
import parsel
import os
import concurrent.futures


def get_response(html_url):
    response = requests.get(url=html_url, headers=headers)
    return response


def get_info(html_url):
    response = get_response(html_url)
    selector = parsel.Selector(response.text)
    lis = selector.css('.chapter__list-box li')
    info_list = []
    for li in list(reversed(lis)):
        chapter_id = li.css('a::attr(data-chapterid)').get()
        chapter_title = li.css('a::text').getall()[-1].strip()
        info_tuple = (chapter_id, chapter_title)
        info_list.append(info_tuple)
    return info_list


def get_img_url(comic_id, chapter_id):
    link = 'https://comic.mkzcdn.com/chapter/content/v1/'
    data = {
        'chapter_id': chapter_id,
        'comic_id': comic_id,
        'format': '1',
        'quality': '1',
        'sign': '3f211d8012cbae79a77164026579b62c',
        'type': '1',
        'uid': '53471616',
    }
    json_data = requests.get(url=link, params=data, headers=headers).json()
    # json_data 字典数据类型, 就可以根据键值对取值
    img_list = json_data['data']['page']
    img_list = [i['image'] for i in img_list]
    return img_list


def save(name, img_url):
    img_content = get_response(img_url).content
    with open(name, mode='wb') as f:
        f.write(img_content)


def get_list_url(html_url):
    html_data = get_response(html_url).text
    selector = parsel.Selector(html_data)
    href = selector.css('.common-comic-item .cover::attr(href)').getall()
    name_id_list = [j.split('/')[1] for j in href]
    name_list = selector.css('.common-comic-item .comic-feature::text').getall()
    list_info = zip(name_id_list, name_list)
    return list_info


def main(home_url):
    list_info = get_list_url(home_url)
    for name_id, name in list_info:
        index_url = f'https://www.mkzhan.com/{name_id}/'
        info_list = get_info(index_url)
        print('正在采集: ', name)
        if not os.path.exists(f'{name}\\'):
            os.mkdir(f'{name}\\')
        for chapter_id, chapter_title in info_list:
            img_list = get_img_url(name_id, chapter_id)
            print(chapter_title)
            page = 1
            for img_url in img_list:
                filename = f'{name}\\{chapter_title}-{page}.jpg'
                save(filename, img_url)
                print(img_url)
                page += 1


if __name__ == '__main__':
    headers = {
        'cookie': '__login_his_sync=0; UM_distinctid=1804ff0bf61af8-097915c0daabb1-6b3e555b-1fa400-1804ff0bf62d60; CNZZDATA1262045698=675826315-1650605442-https%253A%252F%252Fwww.baidu.com%252F%7C1650605442; tourist_expires=1; CNZZDATA1261814609=844855556-1650605900-https%253A%252F%252Fwww.mkzhan.com%252F%7C1650605900; readMode=scroll; redirect_url=%2F212976%2F; cn_1262045698_dplus=%7B%22distinct_id%22%3A%20%221804ff0bf61af8-097915c0daabb1-6b3e555b-1fa400-1804ff0bf62d60%22%2C%22%24_sessionid%22%3A%200%2C%22%24_sessionTime%22%3A%201650610133%2C%22%24dp%22%3A%200%2C%22%24_sessionPVTime%22%3A%201650610133%7D',
        'referer': 'https://www.mkzhan.com/category/?is_vip=1&finish=2&page=2',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36',
    }
    exe = concurrent.futures.ThreadPoolExecutor(max_workers=5)
    for page in range(1, 6):
        url = f'https://www.mkzhan.com/category/?is_vip=1&finish=2&page={page}'
        exe.submit(main, url)
    exe.shutdown()
