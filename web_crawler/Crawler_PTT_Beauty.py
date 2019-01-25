# 爬PTT beauty版

# Get html
import requests
# Crawl and classify
from bs4 import BeautifulSoup
# Regular Expression
import re
# Download img
from urllib.request import urlretrieve
import os

def download_images(articles):
    # EX. 圖片格式: http://imgur.com/OOOO.jpg or https://i.imgur.com/OOOO.gif
    reg_imgur_file = re.compile('http[s]?://[i.]*imgur.com/\w+\.(?:jpg|png|gif)')
    
    for art in articles:
        # if 'download'裡的art.text不存在
        if not os.path.isdir(os.path.join('download_ptt_images', art.text)):
            # 建立'download'目錄下的art.text
            os.mkdir(os.path.join('download_ptt_images', art.text))
        # "art['href']" use the attribute of name to search <a href> tag.
        # "art.text" the text in <a>...</a>.
        print(art['href'], art.text)
        # 抓取圖片
        res = requests.get('https://www.ptt.cc'+art['href'])
        images = reg_imgur_file.findall(res.text)
        print(images)
        # set內將不會有重複元素
        for img in set(images):
            #group(1) = (\w+\.(?:jpg|png|gif))
            ID = re.search('http[s]?://[i.]*imgur.com/(\w+\.(?:jpg|png|gif))', img).group(1)
            print(ID)
            # 下載到指定目錄&檔名
            urlretrieve(img, os.path.join('download_ptt_images', art.text, ID))

def crawler():
    # Confirm 'download' directory not exists.
    if not os.path.isdir('download_ptt_images'):
        os.mkdir('download_ptt_images')
    url = 'https://www.ptt.cc/bbs/Beauty/index.html'
    for round in range(2):
        # Get .html file.
        res = requests.get(url)
        # 'soup' is equivalent to a factory of html.
        soup = BeautifulSoup(res.text, 'html.parser')
        tag_name = 'div.title a'
        articles = soup.select(tag_name)

        download_images(articles)

        # 上一頁的網址
        tag2_name = 'div.btn-group.btn-group-paging a.btn.wide'
        paging = soup.select(tag2_name)
        #print(paging[1]['href'])
        # paging[1]的href
        next_url = 'https://www.ptt.cc'+paging[1]['href']

        url = next_url

crawler()
