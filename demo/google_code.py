# encoding=utf-8
"""
***********************************************
 @ project    : myproject
 @ filename   : google_code.py
 @ author     : LEONE
 @ ide        : PyCharm
 @ createtime : 2019-05-22 10:45:08
 @ desc       : 动态获取google code
***********************************************
"""

import pyotp
def get_totp_token():
    totp = pyotp.TOTP('XXXXXXXXXXXXXXX')
    code = str(totp.now())
    print(code)
    return code
get_totp_token()