import time
from apscheduler.schedulers.blocking import BlockingScheduler


def my_job():
    print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))


sched = BlockingScheduler()
# 每5秒执行一次
# 可以使用修饰器@sched.scheduled_job('interval', seconds=5)代替
# interval 间隔调度（每隔多久执行）;cron 定时调度 ;date 定时调度（任务只会执行一次）
sched.add_job(my_job, 'interval', seconds=5)
sched.start()