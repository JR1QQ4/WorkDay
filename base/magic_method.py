#!/usr/bin/env python
# -*- coding: UTF-8 -*-
class BaseMethod:
    def __new__(cls, *args, **kwargs):
        """
        使用类创建对象时，底层会自动调用这个方法来完成对象的创建
        如果方法中没没有创建对象，也没有返回对象，那么最终创建的对象打印为 None
        一般情况下我们都不会自己去重定义，只有在有特定的需求时才会去用，比如要修改或者控制类创建对象行为时，如实现单例类等等
        """
        print("__________new 方法__________")

    def __init__(self):
        print("__________init 方法__________")


class SingleMethod:
    instance = None

    def __new__(cls, *args, **kwargs):
        print("__________new 方法__________")
        if cls.instance is None:
            # Python3 下的三种写法
            # cls.instance = super(SingleMethod, cls).__new__(cls)
            # cls.instance = super(SingleMethod, cls).__new__(cls, *args, **kwargs)
            cls.instance = super().__new__(cls)
        return cls.instance

    def __init__(self):
        print("__________init 方法__________")


class SecondMethod:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return '({},{})'.format(self.x, self.y)


class DelMethod:
    def __del__(self):
        print("__________del 方法__________")


class CallMethod:
    count = 0

    def __call__(self, *args, **kwargs):
        self.count += 1


class OtherBaseMethod:
    s1 = "Hello, World!"

    def __len__(self):
        print("__len__")
        return 1

    def __repr__(self):
        print("__repr__")
        return self.s1

    def __str__(self):
        print("__repr__")
        return self.s1

    def __bytes__(self):
        print("__bytes__")
        return self.s1.encode()

    def __hash__(self):
        print("__hash__")
        return 2

    def __bool__(self):
        print("__bool__")
        return False


if __name__ == '__main__':
    # a = BaseMethod()  # __________new 方法__________
    # print(a)  # None

    # b = SingleMethod()
    # c = SingleMethod()
    # print(id(b), id(c))  # 1901947769800 1901947769800

    # d = SecondMethod(2, 2)
    # print(d)

    # e = DelMethod()
    # print(e)

    # f = CallMethod()
    # print(f.count)
    # f()
    # print(f.count)

    g = OtherBaseMethod()
    # print(str(g))
    # print(len(g))
    print(repr(g))
    print(bytes(g))
    print(hash(g))
    print(bool(g))
