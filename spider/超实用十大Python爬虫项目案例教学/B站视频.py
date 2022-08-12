"""
[课程内容]： Python爬取B站视频内容

[主讲老师]: 青灯教育-自游老师   

环境：
	python 3.6
	pycharm

	ffmpeg >>> 需要安装 
	
模块使用：
	requests  >>> pip install requests 
	json
	re
	subprocess

[没听懂?]   

+python安装包 安装教程视频   
+pycharm 社区版  专业版 及  激活码免费 

B站弹幕 / B站视频 / Up上传视频 时间播放量等等 / 自动评论 点赞 投币 / 直播自动发送弹幕

B站视频数据:
    1. 音频数据内容
    2. 视频数据内容

通过开发者工具进行抓包分析, 找视频播放地址....

        
"""
import requests
import re
import json
import pprint # 格式化输出的模块
import subprocess


def get_response(html_url):
    """发送请求"""
    headers = {
        'referer': 'https://www.bilibili.com/',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'
    }
    response = requests.get(url=html_url, headers=headers)
    return response


def get_video_info(html_url):
    response = get_response(html_url)
    title = re.findall('<h1 title="(.*?)" class="video-title">', response.text)[0]
    html_data = re.findall('<script>window.__playinfo__=(.*?)</script>', response.text)[0]
    # 正则表达式匹配出来的数据 是列表  [0] 索引取0 取出列表里面的内容 字符串
    # 像json字典数据  把字符串转成json字典数据
    json_data = json.loads(html_data)
    # 403 状态码  没有权限
    # 防盗链的作用:  告诉服务器  我们发送请求的url地址 是从哪里过来的
    # pprint.pprint(json_data)
    # 数据解析 json数据解析 键值对取值
    audio_url = json_data['data']['dash']['audio'][0]['baseUrl']
    video_url = json_data['data']['dash']['video'][0]['baseUrl']
    video_info = [title, audio_url, video_url]
    return video_info


def save(title, audio_url, video_ur):
    """保存数据"""
    # 音频的二进制数据 response.content 获取响应体的二进制数据内容
    # 音频/视频/图片/特定格式的文件 都是以二进制数据进行保存
    audio_content = get_response(audio_url).content
    # 视频的二进制数据
    video_content = get_response(video_ur).content
    with open(title + '.mp3', mode='wb') as f:
        f.write(audio_content)
    with open(title + '.mp4', mode='wb') as f:
        f.write(video_content)
    print('视频内容保存完成.....')


def merge_data(video_name):
    """数据的合并"""
    print('视频合成开始:', video_name)
    # ffmpeg -i 神仙颜值！超美俄国小姐姐-Dashataran!.mp4 -i 神仙颜值！超美俄国小姐姐-Dasha taran!.mp3 -c:v copy -c:a aac -strict experimental output.mp4
    # video_name = video_name.replace(' ', '')
    COMMAND = f'ffmpeg -i {video_name}.mp4 -i {video_name}.mp3 -c:v copy -c:a aac -strict experimental {video_name}output.mp4'
    subprocess.Popen(COMMAND, shell=True)
    print('视频合成结束:', video_name)



url = 'https://www.bilibili.com/video/BV1GW411x7p8'
video_info = get_video_info(url)
save(video_info[0], video_info[1], video_info[2])
merge_data(video_info[0])





