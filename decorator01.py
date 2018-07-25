import inspect
def keyError(func):
    print(func.__name__)
    # 获取参数
    print(inspect.getfullargspec(func).args)
    def inner(name):
        try:
            func(name)
        except KeyError :
            print("=======装饰器KeyError捕捉异常===========")
    return inner

@keyError
def f2(name):
    print("方法2中获取参数： ",name)
    raise KeyError

f2('我是参数')