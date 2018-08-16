from datetime import datetime

# print(datetime.now()) # 2018-08-02 15:21:46.118491
# print(datetime.now().date()) # 2018-08-02
# print(datetime.now().time()) # 15:21:46.118491
# print(datetime.now().timestamp()) # 1533194506.118491
# print(datetime.now().strftime('%Y-%m-%d %X')) # 2018-08-02 15:21:46

# 时间戳转为时间
print(datetime.fromtimestamp(1506654157)) # 2018-08-02 15:21:46.118491

# 字符串转时间
print(datetime.strptime('2018-08-02 15:21:46', '%Y-%m-%d %X'))


