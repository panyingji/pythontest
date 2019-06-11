
# 线程优缺点

"""
两个概念：
1、IO密集型：存在大量的等待时间
2、计算密集型：不存在等待时间

以下代码的结论：
1、IO密集型的，尽量使用并行的方式（线程），可以大大的提高效率
2、计算密集型的，尽量使用串行的方式，使用并行甚至会降低效率（由于不存在等待时间，而CPU又需要不停的切换，增加了耗时）

"""
import time,threading


def foo(something):
    print(something)
    time.sleep(2)


def bar():
    num = 0
    for i in range(100000000):
        num = num + i


start_time = time.time()

# ===============================IO密集型==================================
# 串行方案
# foo("磁盘接受100M数据")
# foo("CPU执行其他任务")

# 并行方案（线程）
# t1 = threading.Thread(target=foo, args=["磁盘接受100M数据"])
# t2 = threading.Thread(target=foo, args=["CPU执行其他任务"])
# t1.start()
# t2.start()
# t1.join()
# t2.join()

# ===============================计算密集型==================================
# 串型方案
# bar()
# bar()

# 并行方案（线程）
t1 = threading.Thread(target=bar)
t2 = threading.Thread(target=bar)
t1.start()
t2.start()
t1.join()
t2.join()


end_time = time.time()

print(end_time - start_time)


