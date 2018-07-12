import threading,time

def task01(args):
    print(threading.current_thread().name,'：正在执行任务','接收参数：',args)
    time.sleep(2)

if __name__ == '__main__':
    print('主线程：'+ threading.current_thread().getName(),'开始')
    t1 = threading.Thread(target=task01,args=('传递参数01',))
    t2 = threading.Thread(target=task01,args=('传递参数02',))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print('主线程：' + threading.current_thread().getName(),'结束')
