import requests
import re
import os
import time

time_now=time.strftime('%Y-%m-%d-%H-%M-%S')
filename = f'{time_now}\\'
if not os.path.exists(filename):
    os.mkdir(filename)

#url_input=input('输入歌单的id:')
url = 'https://music.163.com/playlist?id=7522432948&userid=1355698025'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.66 Safari/537.36 Edg/103.0.1264.44'
}
response = requests.get(url=url,headers=headers)
#print(response.text)

html_data=re.findall('<li><a href="/song\?id=(\d+)">(.*?)</a>',response.text)
for num_id,title in html_data:
    music_url=f'http://music.163.com/song/media/outer/url?id={num_id}.mp3'
    music_content=requests.get(url=music_url,headers=headers).content
    with open(filename + title + '.mp3',mode='wb') as f:
        f.write(music_content)
    print(num_id,title)


