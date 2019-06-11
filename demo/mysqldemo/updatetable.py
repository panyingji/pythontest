# -*- coding:utf-8 -*-
"""
***********************************************
 @ project    : myproject
 @ filename   : updatetable.py
 @ author     : LEONE
 @ ide        : PyCharm
 @ createtime : 2019-05-23 10:19:08
 @ desc       : 更新表
***********************************************
"""

import MySQLdb
# 打开数据库连接
db = MySQLdb.connect("localhost", "root", "123456", "TESTDB", charset='utf8' )
# 使用 cursor()方法获取操作游标
cursor = db.cursor()
# SQL 更新语句
sql = "update student set age = 100 where studentName = 'haha'"
try:
    # 执行 SQL 语句
    cursor.execute(sql)
    # 提交到数据库执行
    db.commit()
except:
    # 发生错误时回滚
    db.rollback()
# 关闭数据库连接
db.close()