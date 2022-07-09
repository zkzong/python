html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""
from bs4 import BeautifulSoup

soup = BeautifulSoup(html, 'lxml')
first_link = soup.a
print(first_link)
print(first_link.find_next_siblings("a"))
first_story_paragraph = soup.find("p", "story")
print(first_story_paragraph.find_next_sibling("p"))
first_link = soup.a
print(first_link)
print(first_link.find_all_next(text=True))
print(first_link.find_next("p"))
first_link = soup.a
print(first_link)
print(first_link.find_all_previous("p"))
print(first_link.find_previous("title"))
