# -*- coding:utf-8 -*-
"""
***********************************************
 @ project    : myproject
 @ filename   : demandtable.py
 @ author     : LEONE
 @ ide        : PyCharm
 @ createtime : 2019-05-23 10:17:32
 @ desc       : 查询数据
***********************************************
"""
import MySQLdb
# 打开数据库连接
db = MySQLdb.connect("localhost", "root", "123456", "TESTDB", charset='utf8' )
# 使用 cursor()方法获取操作游标
cursor = db.cursor()
# SQL 查询语句
sql = """select * from student;"""
try:
    # 执行 SQL 语句
    cursor.execute(sql)
    # 获取所有记录列表
    results = cursor.fetchall()
    for row in results:
        print(row)
except:
    print("Error: unable to fecth data")
    # 关闭数据库连接
    db.close()