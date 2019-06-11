# -*- coding:utf-8 -*-
"""
***********************************************
 @ project    : myproject
 @ filename   : inserttable.py
 @ author     : LEONE
 @ ide        : PyCharm
 @ createtime : 2019-05-23 10:12:05
 @ desc       : 插入表
***********************************************
"""
import MySQLdb

# 打开数据库连接
db = MySQLdb.connect("localhost", "root", "123456", "TESTDB", charset='utf8' )
# 使用 cursor()方法获取操作游标
cursor = db.cursor()
# SQL 插入语句
sql = """INSERT INTO student
VALUES (‘001’,’ haha’, 20, 100)"""
try:
    # 执行 sql 语句
    cursor.execute(sql)
    # 提交到数据库执行
    db.commit()
except:
    # Rollback in case there is any error
    db.rollback()
    # 关闭数据库连接
    db.close()