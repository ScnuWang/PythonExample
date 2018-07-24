def yield01(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n = n + 1

class Yield02(object):
    def __init__(self, max):
        self.max = max
        self.n, self.a, self.b = 0, 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.n < self.max:
            r = self.b
            self.a, self.b = self.b, self.b + self.a
            self.n = self.n + 1
            return r
        raise StopIteration()


def yield03(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        # print(b)
        a, b = b, a + b
        n = n + 1


if __name__ == '__main__':
    print("=====斐波那契数列=====第一种方式=========")
    print("返回结果None;数列值是分开")
    yield01(5)
    print("======斐波那契数列=====第二种方式========")
    print("数据结果储存在一个变量里面，返回结果不会None;但是结构复杂")
    for n in Yield02(5):  # 根据结果发现，这里实际上只初始化了一次Yield02(5)
        print(n)

    print("======斐波那契数列=====第三种方式========")
    print("数据结果储存在一个变量里面，返回结果不会None;但是结构简洁")
    for n in yield03(5):
        print(n)

# 参考博文：https://blog.csdn.net/xjc200808/article/details/51753505
# https://zhuanlan.zhihu.com/p/37257918



