import threading

local = threading.local()

def student():
    std = local.student
    print('线程',threading.current_thread().getName(),'调用',std)

def task(name):
    local.student = name
    student()
if __name__ == '__main__':
    print('主线程：' + threading.current_thread().getName(), '开始')
    t1 = threading.Thread(target=task, args=('Jason',), name='Thread-A')
    t2 = threading.Thread(target=task, args=('Bob',), name='Thread-B')
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print('主线程：' + threading.current_thread().getName(), '结束')
