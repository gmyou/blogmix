#-*- coding: utf-8 -*-
import urllib2
from bs4 import BeautifulSoup
import sys

url = "http://www.naver.com/"
f = urllib2.urlopen(url)
# f = open('sample.html')

def ConvertKorean(s):
    reload(sys)
    sys.setdefaultencoding('utf-8')
    print str(unicode(s))



page = f.read().decode('utf-8', 'ignore')
f.close()

soup = BeautifulSoup(page)

# n = soup.findAll('li', attrs={'class': 'new'})

u = soup.findAll('li', attrs={'class': 'up'})

if (len(u)>0):
	for i in range(len(u)):
		if i == len(u)-1:
			break
		aa = str(u[i].select('a'))
		# TODO extract title
		a = aa.split("title=\"")
		b = a[1].split("\"")
		print b[0]
		
	     # ConvertKorean(i.select('a[title]'))