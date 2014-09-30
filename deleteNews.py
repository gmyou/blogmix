#!/usr/bin/python
# -*- coding: utf-8 -*-

from datetime import date, datetime, timedelta
import MySQLdb

cnx = MySQLdb.connect('localhost', 'user', 'pwd', 'test')
cursor = cnx.cursor()
theMonth = datetime.now().date() + timedelta(months=-1)
add_employee = ("delete from naver_rank_news where cr_date=%s")
data_employee = (theMonth)
# Delete
cursor.execute(add_employee, data_employee)

cnx.commit()
cursor.close()
cnx.close()
