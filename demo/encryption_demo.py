# encoding=utf-8
"""
***********************************************
 @ project    : myproject
 @ filename   : encryption_demo.py
 @ author     : LEONE
 @ ide        : PyCharm
 @ createtime : 2019-05-22 10:45:08
 @ desc       :
***********************************************
"""

# from Crypto import Random
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5 as Cipher_PKCS1_v1_5
import base64

# 数据加密
message = "a1234567"
with open('rsa.pub', 'r') as f:
    public_key = f.read()
    rsa_key_obj = RSA.importKey(public_key)
    cipher_obj = Cipher_PKCS1_v1_5.new(rsa_key_obj)
    cipher_text = base64.b64encode(cipher_obj.encrypt(bytes(message, encoding="utf8")))  # 在Python3中，需要把字符串转为字节串
    print(type(cipher_text))
    print(cipher_text)
    cipher_textstr = cipher_text.decode() # 字节串转变成字符串
    print(cipher_textstr)

# 数据解密
# with open('rsa.key', 'r') as f:
#     private_key = f.read()
#     rsa_key_obj = RSA.importKey(private_key)
#     cipher_obj = Cipher_PKCS1_v1_5.new(rsa_key_obj)
#     random_generator = Random.new().read
#     plain_text = cipher_obj.decrypt(base64.b64decode(cipher_text), random_generator)
#     print('plain text: ', plain_text)