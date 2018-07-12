from multiprocessing import Pool
import os,time

def task01(args):
    time.sleep(10)
    print('父进程PID:', os.getppid(), '子进程PID:', os.getpid(), '接收参数：', args)

def task02(args):
    time.sleep(2)
    print('父进程PID:', os.getppid(), '子进程PID:', os.getpid(), '接收参数：', args)

def task03(args):
    time.sleep(2)
    print('父进程PID:', os.getppid(), '子进程PID:', os.getpid(), '接收参数：', args)

if __name__ == '__main__':
    print('这里是主线程,PID为：', os.getpid())
    p = Pool() #创建进程数
    p.apply_async(task01,args=('hello,task01!',))
    p.apply_async(task02,args=('hello,task02!',))
    p.apply_async(task03,args=('hello,task03!',))
    p.apply_async(task03,args=('hello,task04!',))
    p.apply_async(task03,args=('hello,task05!',))
    p.apply_async(task03,args=('hello,task06!',))
    p.apply_async(task03,args=('hello,task07!',))
    p.close() # 关闭进程池
    p.join()  # 等待所有子进程执行完毕
    print('主线程执行完毕')
