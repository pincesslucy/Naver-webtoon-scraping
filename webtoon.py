# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from bs4 import BeautifulSoup
import requests

url = "https://comic.naver.com/index"
resp = requests.get(url)
soup = BeautifulSoup(resp.text, 'lxml')
rank = soup.select('#realTimeRankFavorite > li > a')
#realTimeRankFavorite > li.rank01 > a
count = len(rank)
i = 0

for ranks in rank:
    i += 1
    print("{0} 위 : {1}".format(i, ranks.text))