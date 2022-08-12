"""
课程内容：python实现12306查票小程序

授课老师： 青灯教育 - 自游老师

环境：
	Python 3.6
	Pycharm

模块使用：
	requests  >>> pip install requests
	pandas >>> pip install pandas
	json

课程必备素材:
    city.json # 文件会用到

[有喜欢听的歌 也可以在公屏上面发一下]
先听一下歌 等一下后面进来的同学 19:35 正式开始讲课

[没听懂?]
课前的开发环境/安装模块/ 找我领取
课后的回放录播 资料找木子老师 免费获得: python10010

+python安装包 安装教程视频   anaconda5.2.0等等 安装包
+pycharm 社区版  专业版 及  激活码免费


0基础学员  扣0
有基础学员 扣1

抢票 或者 查询程序 >>> 爬虫可以应用

基本思路:

一. 这些数据内容是从哪里的?

    通过开发者工具进行抓包分析, 分析具体的数据是从哪里的
        可以通过用搜索 你想要数据内容, 会给你返回相应的数据

二. 代码实现步骤 确定需求 >>> 发送请求 >>> 获取数据 >>> 解析数据 >>> 保存数据
    1. 发送请求, 对于相应的数据包url地址发送请求
    2. 获取数据, 获取响应体json字典数据
    3. 解析数据, 直接通过键值对提取数据
    4. 数据展示
在写代码的过程中, 对于哪一行代码不清楚的地方 可以直接在公屏上面问一下
不建议跟着抄代码

付费系统课程:  基础入门/高级开发/爬虫实战/数据分析/全栈开发

从零基础入门到项目实战系列课程 主要是面向就业的
系统课程学完是 7 个月时间 (可以7个月之后可以直接就业找工作, 找工作可以提前偿还学费)
[报名全套课程学习: 两年学习权限]
全套课程学费是 7880 >>> 优惠学费 7180
可以申请12/24期分期免息 7880/24 = 328 学费/月 328/30 = 10元/天
    每个月 300多就可以跟着老师学习了
    0首付0利息 [每个月支付300多的学费跟着老师学]

9月10号: 教师节优惠活动

爬虫 数据分析 全栈开发 [这方面对于python 对于大众 是最好就业找工作 以及 接外包做副业]
    (游戏开发/辅助/..)

公开课和系统课程有什么区别
    1. 知识面 内容
        系统课程:
            从零基础入门到项目实战系列课程 主要是面向就业的 每一个知识点
            都会详细讲解
        公开课: 简单案例为主
    2. 授课方式:
        系统课程:
        每周 1 3 5 或者 2 4 6  晚上20:00-22:00 直播授课
        课后会提供高清录播回放(可以在腾讯课堂观看)/课件/源码(VIP源码/公开课源码)/文档笔记(电子文档)/软件
        课后老师会提供多对一解答辅导:
            解答方式: 通过QQ/微信/电话 文字 语音 远程操作
            解答时间: 13:00-23:00 10个小时解答时间 除了休息(睡觉)时间以外都会解答 1116
        公开课:
            晚上上课 下午上课
            其他录播老师自己录制的(出意外就没有) 其他资料就没有
        系统课程学习:
            程序员 起步薪资: 10K左右
            学了三个月 (用心跟着老师学): [学Python的达到20K 首先一定的开发经验 其次能力要强]
                1. 可以做副业接单赚钱 >>> (爬虫 数据分析 界面开发外包) 100-1000+不等
                2. 可以去就业 (薪资没那么高估计5-7K左右[学习的知识不够多, 能做的东西不多])
                爬虫无论是就业找是接单 (长远)
                [入门级别]requests bs4 parsel[css选择器/xpath] re selenium [**]远远不够的

                [学会掌握, 你会爬虫]JS逆向 APP爬虫 字体反爬 框架 分布式爬虫 验证码的破解 [基本上没有免费资料]
        公开课学员: 你学三个月 能干啥[会爬小姐姐图片] 没啥用

七个月我能学会吗?
    1. 如果你用心跟着老师学习, 7个月可以保证你学会掌握
    2. 你没时间, 加班(课后录播/课件/老师解答) 课程只是让你学7个月不让你学了?
        2年内都是可以跟着老师学习
    3. 每节课后都会提供作业 (检测大家本节课学习情况)
        每个阶段都会提供考核 (检测本阶段课程知识点 综合能力)
        [考核没有通过, 是需要重修] 是需要接着继续跟着老师学习 (免费)
    你跟着老师学完一期课程之后, 觉得自己不够扎实,是可以继续免费学习的....

老师有[手段]让你用心老师学:
    1. 19:30 会在群通知听课 (会讲解前一节课程 老师布置的作业)
    2. 19:50 班主任老师会私聊通知听课
    3. 20:00 老师会给你打电话通知听课
    4. 没有接听电话 会发短信通知你
    5. 班主任老师会回访....

    以前你要学一个东西:
        跑到教室里面去找老师教 / 挤出大部分时间 (去学校路程中 就30分钟/一个小时)
    在线教育 >>> 主要是利用自己平时空余的时间提升自己 学习知识
        (只有有网络可以直接学习)
0. 模拟登录[登录接口JS加密]  (输入你账号密码 [手动过验证码]) >>> 查票 >>> 预订[选择购买人] >>> [无限刷新 有就买]
1. 打包成exe程序
2. 你可以开发一个软件界面 然后再打包exe pyinstaller
3. 你可以开发一个软件界面 然后再打包apk 手机APP [我没弄过]
微信有网页版 >> 抢红包/聊天记录/防止撤回(别人撤回你一样可以看到)/朋友圈数据
itchat
微信专门的协议

爬取简单网站数据 100-300 >>>100  >>>12节课(用心的学习情况)
    基础入门 五节课
    高级开发 2节 界面 开发
    爬虫课程 前5节课

WARNING: You are using pip version 21.1.3; however, version 21.2.4 is available.
You should consider upgrading via the 'd:\anaconda\python.exe -m pip install --upgrade pip' command.


"""
import requests # 数据请求模块 pip install requests
import pprint # 格式化输出的模块
import pandas as pd   # pip install pandas
import json
f = open('city.json', mode='r', encoding='utf-8')
text = f.read()
city_json = json.loads(text)
# dit = dict(text)
# <class 'str'>   字符串转字典 json
while True:
    from_station = input('请输入出发的城市: ')
    to_station = input('请输入目的城市: ')
    # date = input('请输入查询时间(格式: 2021-09-10):  ')
    # print(city_json[from_station])
    # print(city_json[to_station])
    # print(type(city_json))
    # 模块安装
    # win + R 输入cmd pip install requests
    # 发送请求
    # url = 'https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date=2021-09-11&leftTicketDTO.from_station=CSQ&leftTicketDTO.to_station=LZZ&purpose_codes=ADULT'
    url = 'https://kyfw.12306.cn/otn/leftTicket/query'
    # 字典的形式 ? 非贪婪匹配
    data = {
        'leftTicketDTO.train_date': '2021-09-11',
        'leftTicketDTO.from_station': city_json[from_station],
        'leftTicketDTO.to_station': city_json[to_station],
        'purpose_codes': 'ADULT',
    }
    # 请求头是什么? 作用是什么? 为什么要加
    # 作用是什么 伪装浏览器 (把python代码伪装成浏览器对于发送请求)
    # headers  User-Agent: 浏览器基本信息
    # Cookie 用户信息  host 域名 referer 防盗链
    # 比如 笔趣阁 表情包网站 你都可以不加headers (对某些网站)
    headers = {
        'Cookie': '_uab_collina=163127306978667724605481; JSESSIONID=A05A2A3A8EFF9C5C55C223A9D1D7D0BA; BIGipServerotn=1406730506.64545.0000; guidesStatus=off; highContrastMode=defaltMode; cursorStatus=off; RAIL_EXPIRATION=1631550926458; RAIL_DEVICEID=ej7SCakIhLbC6VTFj3ux4Xqop94p7ZB3tSck8zI1-1vMM076UrMHErYUmIAGysACFMkB_RaphGy8yNqd4iFGlRedEW5kcfQPtJBjNSxzpFw2Lc4F-9Y9kxgIdFPl9EBCHU1vHffV9mzNPNRahlfiR4ICr6F759P8; BIGipServerpassport=837288202.50215.0000; route=c5c62a339e7744272a54643b3be5bf64; _jc_save_fromStation=%u957F%u6C99%2CCSQ; _jc_save_toDate=2021-09-10; _jc_save_wfdc_flag=dc; _jc_save_fromDate=2021-09-11; _jc_save_toStation=%u67F3%u5DDE%2CLZZ',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36'
    }
    # <Response [200]> 返回的是响应体对象 <> 表示对象 200[状态码]表示请求成功
    # 请求参数 params: get请求传递的请求参数  data: post请求需要提交表单
    response = requests.get(url=url, params=data, headers=headers)
    response.encoding = response.apparent_encoding
    # 如果服务器给我们返回的响应体数据 {} 完整的 可以直接获取json字典数据
    # result = response.json()['data']['result']
    # pprint.pprint(response.json())
    # print(response.text)
    # 解析数据 根据键值对进行取值 根据冒号左边的内容 提取冒号右边的内容
    # json 和 字典 数据类型是一样的 json是一种数据存储的格式
    result = response.json()['data']['result']
    lis = []
    for index in result[1:]:
        # 字符串分割方法
        index_list = index.replace('有', 'Yes').replace('无', 'No').split('|') # 返回的列表 可以根据索引位置提取内容
        page = 0
        Num = index_list[3] # 车次
        time_1 = index_list[8] # 发车时间
        time_2 = index_list[9] # 到达时间
        prince_seat = index_list[32]  # 特等座
        first_class_seat = index_list[31]  # 一等座
        second_class = index_list[30]  # 二等座
        Wz = index_list[26] # 无座
        Yz = index_list[29]  # 硬座
        Rw = index_list[23] # 软卧
        Yw = index_list[28] # 硬卧
        dit = {
            'Num': Num,
            'Start': time_1,
            'End': time_2,
            'Top':prince_seat,
            'First':first_class_seat,
            'Second':second_class,
            'Wz': Wz,
            'Yz': Yz,
            'Rw': Rw,
            'Yw': Yw,
        }
        lis.append(dit)
        # print(dit)
    pd.set_option('display.max_rows', None)
    columns = ['Num', 'Start', 'End', 'Top', 'First', 'Second', 'Yz', 'Wz', 'Rw', 'Yw']
    content = pd.DataFrame(lis, columns=columns)
    print(content)






