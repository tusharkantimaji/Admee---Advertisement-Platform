#!C:/Python/python
import pymysql
import sys
try:
    database = pymysql.connect(
        host='localhost', user='root', passwd='', database="admee")
except Exception as e:
    print(e)
    sys.exit(e)
