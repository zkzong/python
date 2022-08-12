"""
[课      题]：Python 爬取抖音无水印视频内容

[主讲老师]: 青灯教育 - 自游老师 上课时间: 20:05

[环境介绍]：
    python 3.8 解释器
    pycharm 2021专业版 >>> 激活码 编辑器

    谷歌浏览器
    谷歌驱动

selenium >>> 驱动 >>> 浏览器
[模块使用]：
    采集一个视频
    requests >>> pip install requests
    re

    采集多个视频
    selenium >>> pip install selenium==3.141.0 (3.141.0) 指定模块版本去安装  使用这个模块安装浏览器驱动
    time

课前福利源码:
    - 浏览器驱动下载安装教程
    - Pycharm使用教程

win + R 输入cmd 输入安装命令 pip install 模块名
先听一下歌 等一下后面进来的同学, 20:05正式开始讲课 [有什么喜欢听得歌曲 也可以在公屏发一下]
---------------------------------------------------------------------------------------------------
听课建议:
    1. 对于本节课讲解的内容, 有什么不明白的地方 可以直接在公屏上面提问, 具体哪行代码不清楚 具体那个操作不明白
    2. 不要进进出出, 早退不仅没有录播, 你还会思路中断
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
第一次听课 1
零基础 2

爬虫案例基本流程思路:

一. 分析数据来源
    1. 确定自己需求 , 我们采集内容是什么? 采集那个网站...  先采集一个视频, 然后再去采集多个视频
    2. 通过开发者工具进行抓包分析....
        I. 开发者工具 网页浏览器自带, F12 或者鼠标右键点击检查选择network
        II. 刷新网页....让网页数据内容重新完整加载一遍 <找视频数据内容>
        III. 通过network下面的media里面找到视频url地址
        IV.  不够.. >>> 分析这个视频url地址从哪里来的... 通过抓包分析, 得到url地址 通过一次编码

二. 代码实现的步骤 爬虫基本四大步骤....
    1. 发送请求, 对于刚刚分析得到url地址发送请求  https://www.douyin.com/video/7086835442330504488
    2. 获取数据, 获取服务器返回响应数据
    3. 解析数据, 提取我们想要视频url地址以及视频标题
    4. 保存数据, 把视频内容保存本地文件夹



就业怎么去找工作? 学什么? 薪资待遇怎么样

零基础入门应届毕业生或者刚入行转行同学
    爬虫工程师
    开发工程师
    数据分析师

爬虫 + 数据分析 + 算法 >>> 数据挖掘  >>> 人工智能算法工程 <高学历 相关专业OK>


兼职接单 怎么接单, 价格怎么样 收入情况.....
    核心编程 高级开发 爬虫 数据分析 (如有条件有想法) + 全栈开发


只要你按时听课, 按时完成作业, 老师可以保证你会掌握.... 8-15K左右薪资是OK
课程教授的内容, 是符合企业招聘需求的...

全套课程学完是7个月的时间... 从零基础入门到项目实战 整个系列课程  专门VIP授课团队 <讲师 + 班主任 售后服务>
    VIP老师: 正心老师 专门代码VIP课程, 青灯教育VIP教授负责人  他一个人可以从头到尾全部教你... <真的大牛>
        自动化办公 人工智能...

全套课程学费
    加清风老师微信: pythonmiss
    1. 预定300学费 领取1000元优惠券  支付 7580...
    2. 提供12期分期免息学习 0利息0手续费 <青灯教育给大家承担>
         7580 / 12 = 631
        京东白条 支付宝花呗 信用卡
    3. 提供两个外包订单  100-1000不等主要是看别人发布情况以及你自己学习情况
        <直接一对一提供外包订单, 让你去接外包, 外包所得钱, 都是属于你自己的>
    4. 专属外包接单群


提供发票 提供合同
授课模式:
    - 在线直播授课 每周3节课 每周 135 或者 246 晚上20:00-22:00 直播授课
        周一上课, 周二写作或者看文档视频巩固复习 周三上课, 周四巩固复习...
    - 课后会提供高清录播回放, 源码 课件 文档笔记 软件工具 <永久观看>
    - 解答辅导 通过微信 文字 语音 远程操作....
    - 每节课后都有作业内容 每个阶段都是有考核
        作业检测本节课学习内容
        考核检测本阶段学习情况
    - 提供免费重修
        如果你考核没有通过, 会强制重修
        如果你觉得自己学得还不够扎实, 可以继续重修
        <免费>
        一遍不行, 学第二遍, 第二遍不行, 学第三遍... <第三遍还有问题, 你这个学习态度有问题>
            事不过三
    提供就业指导
        提供简历修改和制作
        提供企业面试试题
        提供面试技巧
    如果你没来听课的话<也没请假>, 班主任老师会给你电话通知听课


"""
import requests  # 导入数据请求模块 第三方模块 pip install requests
import re  # 导入正则表达式模块  内置模块

from selenium import webdriver
import time  # 时间模块

"""
selenium
    用selenium模块用驱动<浏览器>操作浏览器 
    人怎么去操作浏览器, 怎么去写代码
        1. 打开浏览器
            webdriver.Chrome(executable_path="chromedriver")  括号里面是需要加驱动路径
            如果你驱动放在和代码一个文件夹里面, 可以不用写路径
            或者你的驱动放在python安装目录里面 也可以不用写路径
            其他位置, 都需要指定路径位置
        2. 输入网址
        3. 查看网页内容

requests请求数据,获取服务器返回数据内容
selenium你可以直接根据元素面板去定位数据内容

"""
driver = webdriver.Chrome()  # 实例化一个浏览器对象
driver.get('https://www.douyin.com/user/MS4wLjABAAAAUXBNFnWLvl9T8ylgAbD1auR_o5FL3dF7ic0KMYN9_88')
driver.implicitly_wait(10)


def drop_down():
    for x in range(1, 30, 4):
        time.sleep(1)
        j = x / 9
        js = 'document.documentElement.scrollTop = document.documentElement.scrollHeight * %f' % j
        driver.execute_script(js)


list_1 = [1, 2, 3, 4, 5, 6, 7]
list_1[1:]
drop_down()
lis = driver.find_elements_by_css_selector(
    'div.mwbaK9mv > div:nth-child(2) > ul .ECMy_Zdt')  # 通过 css 选择器查找元素  获取多个li标签返回列表
# url_list = [li.find_element_by_css_selector('a').get_attribute('href') for li in lis]
for li in lis:
    try:
        time.sleep(1)
        url = li.find_element_by_css_selector('a').get_attribute('href')
        """
        爬虫模拟浏览器对于url地址发送请求, 最后获取服务返回响应数据
        发送请求:
            1. 确定url
            2. 模拟伪装
                请求头headers 是可以直接在开发者工具里面复制粘贴 request headers 直接复制
                字典数据类型, 构建完整键值对形式
                user-agent 用户代理 表示浏览器基本身份标识
            3. 请求方式
        
        状态码 200 表示请求成功... 但是不一定得到你想要的数据...
        没有得到你想要数据内容, 是什么原因导致的? <被反爬了> 为什么被反爬了 因为你被识别出来 你是爬虫程序
        
        比如说:
            超市面试试吃 老是你来吃东西<一直你是Ip请求快速>, 不给你吃了 <IP被封>
        """
        # url = 'https://www.douyin.com/video/7087141617865346304'  # 网址
        headers = {
            'cookie': 'douyin.com; ttcid=444dfe8e89ff4d99b0662076ad171c8775; ttwid=1%7CTnFKlrGi3lHjKf5bshFdP9Nwu_Vsiwo-TxvX9NISgj8%7C1642083887%7Cfbfa904ea2900763eb6ac090bdd09014d80840da1ca485bbfea193d5401b330e; MONITOR_WEB_ID=c27b9f4a-4917-4256-be93-e948308467e3; odin_tt=0510c3c4196f54b541a96ac64e8b585b3a755be85057da8a1f3fa068e3f7b75ca2de4345e2b856f1e7b3f9455d86079731fe7d07a9f10890f26855d3674858e1; passport_csrf_token=e0b90cb756903c370592bd558c2b0cf5; passport_csrf_token_default=e0b90cb756903c370592bd558c2b0cf5; s_v_web_id=verify_l268jj46_kc7yYkD6_YHWW_4x4v_9snI_EDE0zro77uRn; AVATAR_FULL_LOGIN_GUIDE_COUNT=1; AVATAR_FULL_LOGIN_GUIDE_TIMESTAMP=1650982839652; AVATAR_FULL_LOGIN_GUIDE_ITA_COUNT=1; AVATAR_FULL_LOGIN_GUIDE_ITA_TIMESTAMP=1650982839652; __ac_nonce=0627ba36600d465d72261; __ac_signature=_02B4Z6wo00f01zrB8EAAAIDCWcswKSh.eLM65fTAAKzW8srQpmSjmL6YX9IsdmMSL4a9EBuyJvIwNMROqFQktniG-Ur-UDPK6wHInC8QKqRYUmyGnflwUXLpKzPgVt2FtREyprGmCDAZLrIpcc; douyin.com; strategyABtestKey=1652269927.635; AB_LOGIN_GUIDE_TIMESTAMP=1652269927510; AVATAR_LOGIN_GUIDE_COUNT=1; _tea_utm_cache_2285=undefined; _tea_utm_cache_6383=undefined; _tea_utm_cache_1300=undefined; pwa_guide_count=3; IS_HIDE_THEME_CHANGE=1; THEME_STAY_TIME=299808; msToken=XGPVAVUHDi9iTEQRjdXuQ0YyetxhHq0c9EH1dLLpttanbCXsNSD0DRxwk9oUB0vZ7LB9vKd-ABi2kAkzj2lCn1x98lJ4iTFbf260RcLav-G4QkhNyq8qV9i3oEJRyc8t; home_can_add_dy_2_desktop=1; msToken=3ALqenaebbJHw7kQDiDG6aRAgVYm5WM1pVGqmyyidbGgYpWRWKn-wQ9tcjoxWrHvwcqoYAx3tQ4IGE1qixdq2ei_fPrirMeeI6HeooU3sGR2wyWQ2OAAh2RejVJOrmpA; tt_scid=Gp0q0JW0LDreTqplgpajIZNHCB0.p1NcVv0hhZBgaGDw4SFxkXGlXfKafiCVmWAWc537',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36'
        }
        response = requests.get(url=url, headers=headers)
        # print(url)
        # <Response [200]> 响应对象 200 状态码 表示请求成功 response.text 获取响应对象文本数据
        # print(response.text)
        """
        数据解析, 提取我们想要数据内容
            re正则表达式 <在付费课程 2.5个小时的内容讲解完>
        re.findall() 调用re模块里面findall方法 去查询匹配数据
            找到所有 >>> 从什么地方去找什么样数据 (.*?) 表示你想要数据内容, 通配符, 可以匹配任意字符(除了换行符以外)
        """
        title = re.findall('<title data-react-helmet="true">(.*?)</title>', response.text, re.S)[0]
        title = re.sub(r'[/\:*?"<>|\n]', '', title)
        video_url = re.findall('src(.*?)%22%7D%2C%7B%22src', response.text)[0]  # 编码的内容获取
        video_url_1 = requests.utils.unquote(video_url).replace('":"', 'https:')  # 解码
        # 编码 requests.utils.quote
        # 就业工作 1 接单赚钱 2
        # print(title)
        # print(video_url)
        # print(video_url_1)
        video_content = requests.get(url=video_url_1, headers=headers).content  # 发送请求获取二进制数据内容
        with open('img\\' + title + '.mp4', mode='wb') as f:
            f.write(video_content)  # 写入内容
            print('正在保存: ', title)
    except Exception as e:
        print(e)
