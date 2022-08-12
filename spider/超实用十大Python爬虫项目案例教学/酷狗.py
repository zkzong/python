"""
[课      题]：爬取海量音乐歌曲，python爬取酷狗音乐网站所有榜单 以及实现搜索下载歌曲

[主讲老师]: 青灯教育 - 自游老师  上课时间: 20:05

[课程亮点]
    1、动态数据抓包演示
    2、json数据解析
    3、requests模块的使用
    4、正则表达式的使用

[环境介绍]：
    python 3.8 解释器
    pycharm 专业版 2021.2

[模块的使用]:
    requests >>> pip install requests 数据请求
    re

win + R 输入cmd 输入安装命令 pip install 模块名
先听一下歌 等一下后面进来的同学, 20:05正式开始讲课 [有什么喜欢听得歌曲 也可以在公屏发一下]
相对应的安装包/安装教程/激活插件/使用教程/学习资料/工具插件 可以加木子老师微信: python10010
---------------------------------------------------------------------------------------------------
听课建议:
    1. 对于本节课讲解的内容, 有什么不明白的地方 可以直接在公屏上面提问, 具体哪行代码不清楚 具体那个操作不明白
    2. 不要跟着敲代码, 先听懂思路, 课后找木子老师领取录播, 然后再写代码
    3. 不要进进出出, 早退不仅没有录播, 你还会思路中断
---------------------------------------------------------------------------------------------------
模块安装问题:
    - 如果安装python第三方模块:
        1. win + R 输入 cmd 点击确定, 输入安装命令 pip install 模块名 (pip install requests) 回车
        2. 在pycharm中点击Terminal(终端) 输入安装命令
    - 安装失败原因:
        - 失败一: pip 不是内部命令
            解决方法: 设置环境变量

        - 失败二: 出现大量报红 (read time out)
            解决方法: 因为是网络链接超时,  需要切换镜像源
                清华：https://pypi.tuna.tsinghua.edu.cn/simple
                阿里云：https://mirrors.aliyun.com/pypi/simple/
                中国科技大学 https://pypi.mirrors.ustc.edu.cn/simple/
                华中理工大学：https://pypi.hustunique.com/
                山东理工大学：https://pypi.sdutlinux.org/
                豆瓣：https://pypi.douban.com/simple/
                例如：pip3 install -i https://pypi.doubanio.com/simple/ 模块名

        - 失败三: cmd里面显示已经安装过了, 或者安装成功了, 但是在pycharm里面还是无法导入
            解决方法: 可能安装了多个python版本 (anaconda 或者 python 安装一个即可) 卸载一个就好
                    或者你pycharm里面python解释器没有设置好
---------------------------------------------------------------------------------------------------
如何配置pycharm里面的python解释器?
    1. 选择file(文件) >>> setting(设置) >>> Project(项目) >>> python interpreter(python解释器)
    2. 点击齿轮, 选择add
    3. 添加python安装路径
---------------------------------------------------------------------------------------------------
pycharm如何安装插件?
    1. 选择file(文件) >>> setting(设置) >>> Plugins(插件)
    2. 点击 Marketplace  输入想要安装的插件名字 比如:翻译插件 输入 translation / 汉化插件 输入 Chinese
    3. 选择相应的插件点击 install(安装) 即可
    4. 安装成功之后 是会弹出 重启pycharm的选项 点击确定, 重启即可生效
---------------------------------------------------------------------------------------------------
零基础同学 0
有基础同学 1

爬虫案例: 固定思路流程

一. 数据来源分析 (由一个数据 一首歌分析 然后找寻全部歌曲规律)
    1. 确定一下自己需求是什么?
    2. 通过开发者工具进行抓包分析...
        I. 分析音频播放地址 音乐url地址 (如果你想要的数据是音频或者视频 可以选择media)
        II.  分析音频url地址 可以从哪个数据包里面得到 一首歌曲数据包
            通过两个歌曲的数据包对比分析 hash id
从一首歌曲 找 数据包 找 请求参数内容

二. 代码实现步骤
    1. 发送请求, 对于榜单url地址发送请求
    2. 获取数据, 获取服务器返回的数据内容
    3. 解析数据, 提取我们想要 音乐 hash id 这两个参数

    4. 发送请求, 对于音乐数据包发送请求
    5. 获取数据, 获取服务器返回的数据内容
    6. 解析数据, 提取我们想要音乐标题 以及 音频播放地址

    7. 保存数据

招生宣传.....
    系统课程内容, 付费课程, 从0基础入门到项目实战 面向就业找工作 系统课程

学历建议大专以上
就业找工作: 学完7个月的时间, 可以找8-15K薪资左右工作 (掌握课程内容就可以了)
    应届毕业生 8-15K 左右
    1-3年工作经验: 15-30K左右
    3-5年工作经验: 20-40K左右
    爬虫 数据分析 开发 [这三个当中招聘又是最多的]
接外包兼职: 跟着老师最少3个月时间,可以开始接外包赚钱 月收入 1000-3000 左右

招聘的需求, 我们课程里面都是教授了的.....

你可以保证你跟着老师学习, 按时听课, 按时完成课后作业吗? 阶段考核... 我也可以保证你能够学会掌握

VIP授课方式以及服务:
    - 在线直播授课 每周 135 或者 246 晚上20:00-22:00 直播授课 平均每节课 2.5个小时左右
    - 课后会提供高清录播回放, 源码 课件 笔记 文档 软件工具一应俱全 永久权限
    - 解答辅导 通过微信 文字 语音 远程操作等方式 解答辅导  我自游凌晨三点前找我都可以 给你解答辅导.. (国外的VIP)
    - 提供免费重修学习权限....
        如果你跟着老师学完一期课程之后,考核没有通过, 强制重修 在跟着学习一期课程 并且免费的
        古人云 事不过三.... (直播学习权限) 两年学习辅导服务 不存在二次收学费...
    - 提供打电话通知听课
    - 提供就业指导
    - 提供外包接单渠道 外包群
    - 发票 合同 ....

现在报名优惠后学费 7880 学费不需要一定要求你一次性支付 0利息0手续费
    可以找清风申请 12期分期免息学习, 通过京东白条 支付宝花呗 信用卡 腾讯课堂官方分期渠道
    7880/12 = 656/月学费  每天一杯奶茶就可以跟着学习了

    找清风去申请18期分期免息学习  437的学费

公开课作为一个案例演示效果, 告诉大家可以用python实现什么内容 什么东西


"""
# 导入数据请求模块
import requests
# 导入正则
import re
# 导入格式化输出模块
import pprint


home_url = 'https://www.kugou.com/yy/html/rank.html'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36'
}
response = requests.get(url=home_url, headers=headers)
# print(response.text)
urls = re.findall('<a title="(.*?)"  hidefocus="true" href="(.*?)"', response.text)
for title, list_url in urls[11:]:
    print(title, list_url)
    """
    1. 发送请求, 对于榜单url地址发送请求
        Python模拟浏览器去对于url地址发送请求
        user-agent: 用户代理的意思 表示浏览器基本身份信息
        
    """
    # url = 'https://www.kugou.com/yy/html/rank.html'
    # 通过requests里面get请求方法对于url地址发送请求, 并且携带上headers请求参数伪装, 最后用response接收返回数据
    response = requests.get(url=list_url, headers=headers)
    # <Response [200]> 返回response响应的对象  200 表示请求成功
    # 2. 获取数据, 获取服务器返回的数据内容(文本数据内容)
    # print(response.text)
    """
    3. 解析数据, 提取我们想要 音乐 hash id 这两个参数
        正则表达式 re 可以直接对于字符串数据进行提取
        .*? 通配符 可以匹配任意字符(除了\n换行符)
    
    就业 1
    兼职 2
    毕设都是 爬虫 + 数据分析
    for循环可以遍历一个列表
    
    毕设 工作室 企业 相应的数据
        爬虫和数据分析 兼职订单多一些
        网站开发 价格一般 1000+以上 大多公司或者工作室 后台信息管理系统 官网...
        做兼职:
            1. 价格怎么定
                根据需求 简单 100-300 爬取链接二手房数据
                中等 300-100(拉勾 boss招聘数据) 左右
                难度 1000+以上不等 抖音 电商平台 JS逆向反爬比较严重 app数据采集
            2. 学那些东西
                GUI桌面应用开发 Tk pyqt
                核心编程 高级开发 爬虫实战 数据分析 你有条件 有想法 多学全栈开发
            3. 怎么去接外包
                接外包平台
                淘宝 闲鱼  接单群(***慎重选择)
                如果你是青灯付费学员 专属接单群 以及 专属外包福利
    """
    hash_list = re.findall('"Hash":"(.*?)"', response.text)
    album_id_list = re.findall('"album_id":(.*?),', response.text)
    zip_data = zip(hash_list, album_id_list)  # zip() 函数打包一下
    for Hash, album_id in zip_data:
        # print(Hash, album_id)
        # 4. 发送请求, 对于音乐数据包发送请求
        index_url = 'https://wwwapi.kugou.com/yy/index.php'
        # 如果请求url过长, 可以分开写, url问号前面可以用变量接收, 问号属于请求参数 构建成字典
        # 等号左边都是自定义变量, 你想要data也可以 想params也可以
        params = {
            'r': 'play/getdata',
            'hash': Hash,
            'dfid': '0jJ7pp4NRPlq14bXWB1qUaKJ',
            'appid': '1014',
            'mid': 'efed59987aff73607736bb734a1a732e',
            'platid': '4',
            'album_id': album_id,
            '_': '1649333625329',
        }
        response_1 = requests.get(url=index_url, params=params, headers=headers)
        # print(response_1.json())
        # 5. 获取数据 字典数据 字典取值 键值对取值 根据冒号左边的键, 提取冒号右边的值
        # pprint.pprint(response_1.json())
        # 6. 解析数据
        audio_name = response_1.json()['data']['audio_name']  # 歌曲名字
        play_url = response_1.json()['data']['play_url']
        if play_url: # 判断是否有
            print(audio_name, play_url)
            # 7. 保存数据
            audio_name = re.sub(r'[/\:"?<>|*]', '', audio_name)
            music_content = requests.get(url=play_url, headers=headers).content  # 获取音乐二进制数据内容
            with open('music\\' + audio_name + '.mp3', mode='wb') as f:
                f.write(music_content)

