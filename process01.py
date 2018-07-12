from multiprocessing import Process
import os
def task(args):
    print('父进程PID:',os.getppid(),'子进程PID:',os.getpid(),'接收参数：',args)

if __name__ == '__main__':
    print('这里是主进程,PID为：',os.getpid())
    p = Process(target=task,args=('hello,world!',))
    p.start()
    p.join()
    print('主进程执行完毕')