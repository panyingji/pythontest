# -*- coding:utf-8 -*-
"""
***********************************************
 @ project    : myproject
 @ filename   : createtable.py
 @ author     : LEONE
 @ ide        : PyCharm
 @ createtime : 2019-05-23 09:59:54
 @ desc       : 创建表
***********************************************
"""

import MySQLdb

# 打开数据库连接
db = MySQLdb.connect("localhost", "root", "123456", "TESTDB", charset='utf8' )
# 使用 cursor()方法获取操作游标
cursor = db.cursor()
# 如果数据表已经存在使用 execute() 方法删除表。
cursor.execute("DROP TABLE IF EXISTS student")
# 创建数据表 SQL 语句
sql = """CREATE TABLE student (
id CHAR (50) NOT NULL,
studentName CHAR (20),
age INT,
score CHAR (1));"""
cursor.execute(sql)
# 关闭数据库连接
db.close()