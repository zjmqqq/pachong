import os,django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "untitled1.settings")# project_name 项目名称
django.setup()

from  pachong.models import movie

import urllib.request
from bs4 import BeautifulSoup

num=0
url="https://movie.douban.com/top250?start="
MovieList = []
_id = 0
ua_headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"
}
while num <= 225:
    request = urllib.request.Request(url+str(num), headers = ua_headers)
    response =urllib.request.urlopen(request)
    html = response.read().decode("utf-8")
    soup=BeautifulSoup(html,"html.parser")
    onenodes=soup.select("div .item")
    for onenode in onenodes:
        titles=onenode.find_all("div",class_="info")
        for title in titles:
            title1s=title.find_all("span",class_="title")
            title2=title.find_all("span",class_="other")[0].text
            for i in range(len(title1s)):
                title2=title1s[i-len(title1s)+1].text+title2
            mmovie=movie()
            print(title2)
            mmovie.name=title2
            print(_id)
            try:
                print(title.find("p",class_="quote").text)
                mmovie.content = title.find("p", class_="quote").text
            except:
                print("无")
                mmovie.content = "暂无"
            mmovie.save()
            _id += 1

    num=num+25