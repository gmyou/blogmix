#-*- coding: utf-8 -*-
import urllib
import urllib2
import time

referer = "http://www.naver.com"
def goUrl(routine, proxy, url):
	global referer

	site= "http://search.naver.com/search.naver"
	hdr = {'User-Agent': 'Mozilla/5.0'}
	req = urllib2.Request(site, headers=hdr)
	req.add_header('Referer', referer)
	req.set_proxy(proxy, 'http')

	referer = url

	page = urllib2.urlopen(req)
	print routine, url, page.getcode()

	res = page.read().decode('utf-8')
	

	time.sleep(5)


values = {'query':'줄리엔강'}
data = urllib.urlencode(values)
goUrl('search', '94.203.147.218:8080', 'http://search.naver.com/search.naver?where=nexearch&%s&sm=top_lve&ie=utf8&'%data)
goUrl('viewmore', '94.203.147.218:8080', 'http://cafeblog.search.naver.com/search.naver?where=post&%s&ie=utf8&sm=tab_nmr&nso='%data)

for p in range(11, 110, 10):
	goUrl('viewmore', '94.203.147.218:8080', 'http://cafeblog.search.naver.com/search.naver?where=post&sm=tab_pge&%s&st=sim&date_option=0&date_from=&date_to=&dup_remove=1&post_blogurl=&post_blogurl_without=&srchby=all&nso=&ie=utf8&start=%d' % (data, p))
