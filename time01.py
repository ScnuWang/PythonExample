import time

print(time.time()) # 1534405932.169806

print(time.mktime(time.localtime())) #1534405932.0

print(time.localtime())# time.struct_time(tm_year=2018, tm_mon=8, tm_mday=16, tm_hour=15, tm_min=52, tm_sec=12, tm_wday=3, tm_yday=228, tm_isdst=0)

print(time.localtime(time.time()))# time.struct_time(tm_year=2018, tm_mon=8, tm_mday=16, tm_hour=15, tm_min=52, tm_sec=12, tm_wday=3, tm_yday=228, tm_isdst=0)

print(time.gmtime()) # 格林威治时间# time.struct_time(tm_year=2018, tm_mon=8, tm_mday=16, tm_hour=7, tm_min=52, tm_sec=12, tm_wday=3, tm_yday=228, tm_isdst=0)
print(time.gmtime(time.time())) # time.struct_time(tm_year=2018, tm_mon=8, tm_mday=16, tm_hour=7, tm_min=52, tm_sec=12, tm_wday=3, tm_yday=228, tm_isdst=0)

print(time.strptime('2018-06-05 14:41:06', '%Y-%m-%d %X')) # time.struct_time(tm_year=2018, tm_mon=6, tm_mday=5, tm_hour=14, tm_min=41, tm_sec=6, tm_wday=1, tm_yday=156, tm_isdst=-1)

print(time.strftime('%Y-%m-%d %X')) # 2018-08-16 15:52:12
print(time.strftime('%Y-%m-%d %X',time.localtime())) # 2018-08-16 15:52:12
print(time.asctime(time.localtime())) # Thu Aug 16 15:52:12 2018
print(time.ctime(time.time())) # Thu Aug 16 15:52:12 2018
