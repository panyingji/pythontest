import time,threading,random

account_balance = 500   # 银行卡账户余额

r = threading.Lock()    # 定义同步锁


def option_num(num):
    global account_balance
    r.acquire()         # 上锁
    balance = account_balance
    time.sleep(random.randint(0, 10) * 0.1)  # 并不知道要计算多久
    balance += num
    account_balance = balance
    r.release()         # 解锁


t1 = threading.Thread(target=option_num, args=[10000])
t2 = threading.Thread(target=option_num, args=[-300])

t1.start()
t2.start()
t1.join()
t2.join()

print("所有子线程运行完毕")
print(f"最终账户余额为：{account_balance}")