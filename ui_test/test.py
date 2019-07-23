# -*- coding:utf-8 -*-
"""
***********************************************
 @ project    : myproject
 @ filename   : test.py
 @ author     : LEONE
 @ ide        : PyCharm
 @ createtime : 2019-07-19 11:31:40
 @ desc       : 
***********************************************
"""
with open('ApiAutomatedTestReport_2019-07-02_16_07_43.html',encoding='utf-8') as f:
    html_doc = f.read()

from bs4 import BeautifulSoup

soup = BeautifulSoup(html_doc,'html5lib')
t = soup.find('title')
print(t)
print(type(t))
print(t.string)
print(t.get_text())
print(soup.title.string)
print(soup.title.get_text())
print('---------------')

# 打印title元素的父节点
print(soup.title.parent)
print(soup.title.parent.get_text())
print('---------------')


# 获取元素的属性值
print(soup.h3['style'])
print(soup.find_all('p'))
print(soup.find_all('p')[1])
print(soup.find_all('p')[1]['class'])
print(type(soup.find_all('p')[1]['class']))
print('-----------------')

a = soup.find('a')
print(a)
print(a.name)
# 返回元素的文本内容
print(a.string)
print(a.get_text())
print('-------------')

print(soup.a)
print(soup.a.get_text())
print(type(a))
print('-------------')

print(soup.find('canvas',id="circle1"))