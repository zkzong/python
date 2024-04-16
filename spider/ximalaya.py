import requests
from bs4 import BeautifulSoup

# todo
url = 'https://www.ximalaya.com/sound/722417311'
response = requests.get(url)
if response.status_code == 200:
    html_content = response.text

    soup = BeautifulSoup(html_content, 'html.parser')

    audio_links = soup.select('audio source')
    for link in audio_links:
        audio_url = link['src']
        print(audio_url)
        audio_file = requests.get(audio_url)
        with open('audio.mp3', 'wb') as f:
            f.write(audio_file.content)
