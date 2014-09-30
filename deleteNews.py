#!/usr/bin/python
# -*- coding: utf-8 -*-

import _mysql
import sys
import date

theday = date.today()
print(theday)

try:
    con = _mysql.connect('localhost', 'user', 'password', 'database')
    print ("delete from naver_rank_news where cr_date='"+theday+"'")
    con.query("delete from naver_rank_news where cr_date='"+theday+"'")
    result = con.use_result()

    print "MySQL version: %s" % \
        result.fetch_row()[0]

except _mysql.Error, e:

    print "Error %d: %s" % (e.args[0], e.args[1])
    sys.exit(1)

finally:

    if con:
        con.close()
