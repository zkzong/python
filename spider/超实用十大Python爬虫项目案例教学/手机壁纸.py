"""
[课程内容]: python爬取超清画质手机壁纸

[授课老师]: 青灯教育-自游  [上课时间]: 14:35

[开发环境]:
    Python 3.8
    Pycharm

[模块使用]:
    requests >>> pip install requests 数据请求
    parsel >>> pip install parsel 解析模块 (提取数据)

先听一下歌 等一下后面进来的同学, 14:35正式开始讲课 [有什么喜欢听得歌曲 也可以在公屏发一下]
相对应的安装包/安装教程/激活码/使用教程/学习资料/工具插件 可以加木子老师微信: python10010
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
                阿里云：http://mirrors.aliyun.com/pypi/simple/
                中国科技大学 https://pypi.mirrors.ustc.edu.cn/simple/
                华中理工大学：http://pypi.hustunique.com/
                山东理工大学：http://pypi.sdutlinux.org/
                豆瓣：http://pypi.douban.com/simple/
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

爬虫基本流程:

一. 数据来源分析
    1. 爬取网站是什么  想要获取网站什么样数据内容
        比如爬取图片  从一张图片去分析
    通过开发者工具进行抓包分析, 对比我们想要图片url地址一些参数

二. 爬虫代码实现步骤:
    1. 发送请求, 对于分析得到url地址发送请求
        请求网址
        请求方式
        请求头参数 >>> 伪装 可以把python代码伪装成浏览器(客户端)发送请求
            如果不进行伪装会有什么后果 >>> 不会给你返回你想要数据
    2. 获取数据, 获取response服务器返回响应数据
    3. 解析数据, 提取我们想要数据内容 图片url地址 以及 图片标题
    4. 保存数据, 把图片数据保存到本地

基础语法:
    for循环
    自定义变量 赋值
    字符串格式化方法
    字典创建
    函数关键字传参
    zip内置函数
    输出函数

文件操作
requests简单使用 get请求 获取数据
parsel 简单使用 css语法

"""
# 导入数据请求模块  导入模块没有使用, 灰色待机状态
import requests   # pip install requests
# 导入数据解析模块
import parsel   # pip install parsel
"""
1. 发送请求
headers 请求头参数, 可以开发者工具里面直接进行复制, 其次headers字典数据类型, 键值对
user-agent: 用户代理 表示浏览器基本身份标识
cookie: 用户信息, 检测用户是否有登陆账号
"""
for page in range(2, 11):
    url = f'https://sj.enterdesk.com/woman/{page}.html'
    headers = {
        'cookie': 't=f2cf055ce8713058cbfdbd1561c38e86; r=1281; Hm_lvt_86200d30c9967d7eda64933a74748bac=1645625923,1646892448; Hm_lpvt_86200d30c9967d7eda64933a74748bac=1646894465',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'
    }
    response = requests.get(url=url, headers=headers)   #  <Response [200]> 返回响应对象 200状态码标识请求成功
    """
    2. 获取数据, 获取服务器返回数据内容, 获取响应对象文本数据  字符串数据
        返回数据内容, 和我们在开发者工具里面看到不一样  说明你被服务器识别出来是你爬虫程序, 所以他没有给你返回数据
        
    """
    # print(response.text)
    """
    3. 解析数据
        css选择器 xpath re 三种解析方式都可以去用 选择最适合
    css选择器: 根据标签属性提取数据内容
    对于获取response.text 进行数据类型转换 转成 selector 对象 <Selector xpath=None data='<html xmlns="http://www.w3.org/1999/x...'>
    attr() 属性选择器  .egeli_pic_li .egeli_pic_dl dd a img 都是定位标签, 告诉它是哪一个标签
    img::attr(src) 取img标签里面的src属性数据
    getall()  获取所有标签内容数据 返回列表数据类型
    
    """
    selector = parsel.Selector(response.text)
    src = selector.css('.egeli_pic_li .egeli_pic_dl dd a img::attr(src)').getall()
    alt = selector.css('.egeli_pic_li .egeli_pic_dl dd a img::attr(alt)').getall()
    for img_url, title in zip(src, alt):
        img_url = img_url.replace('edpic_360_360', 'edpic_source')
        # 4. 保存数据
        img_content = requests.get(url=img_url, headers=headers).content  # 获取二进制数据内容
        with open('img\\' + title + '.jpg', mode='wb') as f:
            f.write(img_content)
        print(img_url, title)


