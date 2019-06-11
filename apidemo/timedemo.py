import datetime
timestamp = 1234567890
dt = datetime.datetime.utcfromtimestamp(timestamp) # 时区为UTC
dt = datetime.datetime.fromtimestamp(timestamp) # 时区为本地时区
print(dt)