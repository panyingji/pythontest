# encoding=utf-8
"""
***********************************************
 @ project    : myproject
 @ filename   : passwd_encrypt.py
 @ author     : LEONE
 @ ide        : PyCharm
 @ createtime : 2019-05-22 10:45:08
 @ desc       :
***********************************************
"""

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5 as Cipher_PKCS1_v1_5
import base64


def passwdencry(passwd):
    with open('rsa.pub', 'r') as f:
        public_key = f.read()
        rsa_key_obj = RSA.importKey(public_key)
        cipher_obj = Cipher_PKCS1_v1_5.new(rsa_key_obj)
        cipher_text = base64.b64encode(cipher_obj.encrypt(bytes(passwd, encoding="utf8")))  # 在Python3中，需要把字符串转为字节串
        password = cipher_text.decode()
        return password