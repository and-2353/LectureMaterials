# requests: 標準ライブラリ
# bs4: 外部ライブラリ
# 
# pip install beautifulsoup4 でinstall

import requests
from bs4 import BeautifulSoup

load_url = "https://ja.wikipedia.org/wiki/%E6%97%A5%E6%9C%AC"
html = requests.get(load_url)
soup = BeautifulSoup(html.content, "html.parser")

print(soup)