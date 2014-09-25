def findBlog(proxy):
    global keyword
    global blogurl
 
    
 
    for p in range(11, 100, 10):
        print p
        url = 'http://cafeblog.search.naver.com/search.naver?where=post&sm=tab_pge&%s&st=sim&date_option=0&date_from=&date_to=&dup_remove=1&post_blogurl=&post_blogurl_without=&srchby=all&nso=&ie=utf8&start=%d' % (keyword, p)
 
        proxies = {"http":"http://%s" % proxy}
        headers = {'User-agent' : 'Mozilla/5.0'}
 
        proxy_support = urllib2.ProxyHandler(proxies)
        opener = urllib2.build_opener(proxy_support, urllib2.HTTPHandler(debuglevel=1))
        urllib2.install_opener(opener)
 
        request=urllib2.Request(naver, None, headers)
        request.add_header('cookie','')
 
        try: response = urllib2.urlopen(request)
        except urllib2.URLError, e: print(e.reason)
 
        print response.getcode()
 
        # page = response.read().decode('utf-8', 'ignore')
        # response.close()
 
        # soup = BeautifulSoup(page)
 
        # # sh_blog_title _sp_each_url _sp_each_title
        # # http://gmyou71.blog.me/220124481686
 
        # content = soup.findAll('a', attrs={'class': 'sh_blog_title _sp_each_url _sp_each_title'})
 
        # for c in content:
        #     print c['item'] 
