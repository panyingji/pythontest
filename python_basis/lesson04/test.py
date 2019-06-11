# encoding=utf-8
"""
***********************************************
 @ project    : myproject
 @ filename   : test.py
 @ author     : LEONE
 @ ide        : PyCharm
 @ createtime : 2019-05-22 10:45:08
 @ desc       :
***********************************************
"""

# for i in range(1, 10):
#     for j in range(1, i + 1):
#         print(u'{}x{}={}\t'.format(i, j, i * j), end='')
#     print()


def func():
    for i in range(1, 10):
        for j in range(1, i + 1):
            print(u'{}x{}={}\t'.format(i, j, i * j), end='')
        print()
    return [1,2,3,4,5]


res = func()
print(res)



#字符串对象的常用方法
#count
# str1 = 'abcdefa'
# print(str1.count('a'))


def telphonenum():
    Phone_YiDong = ['134', '135', '136', '137', '138', '139', '147', '150', '151', '152', '157', '158', '159', '178',
                    '182', '183', '184', '187', '188', '198']
    Phone_LianTong = ['130', '131', '132', '155', '156', '145', '185', '186', '166', '176']
    Phone_DianXin = ['133', '149', '153', '180', '181', '189', '199', '173', '177']
    phone = input('请输入您的手机号：')
    if len(phone) == 11 and phone.isdigit():
        if phone[:3] in Phone_YiDong:
            print('输入的手机号为移动用户！')
        elif phone[:3] in Phone_LianTong:
            print('输入的手机号为联通用户！')
        elif phone[:3] in Phone_DianXin:
            print('输入的手机号为电信用户！')
        elif not phone.isalpha():
            print('输入的手机号不能为字母和数字！')
        else:
            print('输入的手机号不是中国大陆用户！')
    elif phone.isalpha():
        print('手机号不能输入纯字母！')
    elif not phone.isalnum():
        print('输入的手机号不能包含特殊字符！')
    elif not phone.isalpha() and not phone.isdigit():
        print('手机号不能输入字母和数字组合！')
    else:
        print('手机号必须为11位纯数字！')


telphonenum()

str1 = 'abcdefg'
print(str1.startswith('a'))
print(str1.endswith('g'))

#查找元素位置
#find,返回的是元素的下标，如果元素不存在则返回-1
str2 = 'abcdef'
print(str2.find('d'))
print(str2.find('x'))

#str.join将序列类型的字符串以某种格式进行拼接，功能比“+”更强大
str3 = ' '.join(['I','love','you!'])
print(str3)

#str.split,将序列类型以某种格式进行切割，作为切片操作的辅助，1.切点消失，2.返回list,3.如果切点不存在，则不操作，仍然返回list
info = 'Name is Tom'
res = info.split(' ')
print(res)
print(res[0])
res1 = info.split('x')
print(res1[0])
# print(res1[1])               #注意：次数下标会越界

#字母大小写转换
str4 = 'China'
str5 = 'CHINA'
print(str4.upper())
print(str5.lower())

#替换字符串
str6 = 'Name is Tom'
print(str6.replace('Tom','Jack'))

aList = [1,2,3]
print(max(aList))
