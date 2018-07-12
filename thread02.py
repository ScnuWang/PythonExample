import time,threading

number = 6
lock = threading.Lock()
def change_num():
    print(threading.current_thread().getName(),'进入方法')
    global number
    lock.acquire() # 获取锁
    try:
        #     尽可能让线程切换的次数够多
        for i in range(100000):
            number = number + 8
            number = number - 8
    finally:
        lock.release() # 确保锁一定会被释放

if __name__ == '__main__':
    print('主线程：' + threading.current_thread().getName(), '开始')
    print('---------',number,'----------')
    t1 = threading.Thread(target=change_num)
    t2 = threading.Thread(target=change_num)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print('---------', number, '----------')
    print('主线程：' + threading.current_thread().getName(), '结束')

''' 可能出现的错误结果
主线程：MainThread 开始
--------- 6 ----------
Thread-1 进入方法
Thread-2 进入方法
--------- -2 ----------
主线程：MainThread 结束

主线程：MainThread 开始
--------- 6 ----------
Thread-1 进入方法
Thread-2 进入方法
--------- 14 ----------
主线程：MainThread 结束

'''