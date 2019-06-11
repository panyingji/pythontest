# -*- coding:utf-8 -*-
"""
***********************************************
 @ project    : myproject
 @ filename   : connect.py
 @ author     : LEONE
 @ ide        : PyCharm
 @ createtime : 2019-05-23 09:57:13
 @ desc       : 数据库连接
***********************************************
"""

import MySQLdb

db = MySQLdb.connect("localhost","root","123456","testdb",charset="utf8")

# 使用 cursor()方法获取操作游标
cursor = db.cursor()
# 使用 execute 方法执行 SQL 语句
cursor.execute("SELECT VERSION()")
# 使用 fetchone() 方法获取一条数据
data = cursor.fetchone()
print("Database version : %s " % data)
# 关闭数据库连接
db.close()