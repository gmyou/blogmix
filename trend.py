#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib
import urllib2
import time

referer = "http://www.naver.com"
cookie = ""
def goUrl(routine, proxy, url):
    global referer
    global cookie

    proxies = {"http":"http://%s" % proxy}
    headers = {'User-agent' : 'Mozilla/5.0'}


    if (url != referer):
	    proxy_support = urllib2.ProxyHandler(proxies)
	    opener = urllib2.build_opener(proxy_support, urllib2.HTTPHandler(debuglevel=1))
	    urllib2.install_opener(opener)

    request=urllib2.Request(url, None, headers)

    if (url == referer):
        request.add_header('cookie','')
    else:
        request.add_header('cookie', cookie)


    site= "http://search.naver.com/search.naver"
    request.add_header('Referer', referer)
    referer = url

    page = urllib2.urlopen(request)
    print routine, url, page.getcode()

    # res = page.read().decode('utf-8')
	
    try: response = urllib2.urlopen(request)
    except URLError, e: print(e.reason)
    
    cookie = response.headers.get('Set-Cookie')
    # data = response.read()
    print '\n'
    # print '\t-------------- data'
    # print data
    print '\t-------------- cookie'
    print cookie
    print '\t-------------- status'
    print response.getcode()

    time.sleep(5)


values = {'query':'줄리엔강'}
data = urllib.urlencode(values)
goUrl('search', '94.203.147.218:8080', 'http://search.naver.com/search.naver?where=nexearch&%s&sm=top_lve&ie=utf8&'%data)
goUrl('viewmore', '94.203.147.218:8080', 'http://cafeblog.search.naver.com/search.naver?where=post&%s&ie=utf8&sm=tab_nmr&nso='%data)

for p in range(11, 100, 10):

	goUrl('viewmore', '94.203.147.218:8080', 'http://cafeblog.search.naver.com/search.naver?where=post&sm=tab_pge&%s&st=sim&date_option=0&date_from=&date_to=&dup_remove=1&post_blogurl=&post_blogurl_without=&srchby=all&nso=&ie=utf8&start=%d' % (data, p))
search.naver?where=post&sm=tab_pge&%s&st=sim&date_option=0&date_from=&date_to=&dup_remove=1&post_blogurl=&post_blogurl_without=&srchby=all&nso=&ie=utf8&start=%d' % (data, p))
