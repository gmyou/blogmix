#-*- coding: utf-8 -*-
import urllib2
from bs4 import BeautifulSoup
import sys

url = "http://www.naver.com/"

try:
    f = urllib2.urlopen(url)
except urllib2.HTTPError:
    pass

reload(sys)
sys.setdefaultencoding('utf-8')

page = f.read().decode('utf-8', 'ignore')
f.close()

soup = BeautifulSoup(page)

data = soup.find('ol', attrs={'id': 'realrank'}).findAll('a')
for tag in data[:-1]:
    try:
        print str(unicode(tag['title']))
    except KeyError:
        pass
