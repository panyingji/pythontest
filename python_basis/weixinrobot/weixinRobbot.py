# encoding=utf-8
"""
***********************************************
 @ project    : myproject
 @ filename   : weixinrobbot.py
 @ author     : LEONE
 @ ide        : PyCharm
 @ createtime : 2019-05-22 10:45:08
 @ desc       :
***********************************************
"""

from wxpy import *
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

chatbot = ChatBot("deepThought")  # 用于回复消息的机器人
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train("chatterbot.corpus.chinese")  # 使用该库的中文语料库
bot = Bot(cache_path=True)  # 用于接入微信的机器人
group_2 = bot.groups("深夜喝粥群")[0]  # 进行测试的群
group_2.send("大家好,我是人工智能机器人")


# MyFriend = bot.friends("极策科技-潘呈")[0]
@bot.register(group_2)
def reply_my_friend(msg):
    print(msg)
    return chatbot.get_response(msg.text).text  # 使用机器人进行自动回复


# 堵塞线程，并进入 Python 命令行
embed()
