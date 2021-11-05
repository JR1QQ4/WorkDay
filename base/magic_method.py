#!/usr/bin/env python
# -*- coding: UTF-8 -*-
class Person:
    instances_created = 0
    _singleton = None

    # __init__方法中除了self之外定义的参数，都将与__new__方法中除cls参数之外的参数是必须保持一致或者等效
    def __new__(cls, *args, **kwargs):
        print("__new__():", cls, args, kwargs)
        # 如果要得到当前类的实例，应当在当前类中的 __new__() 方法语句中调用当前类的父类的 __new__() 方法
        if cls._singleton is None:
            cls._singleton = super().__new__(cls)
        cls._singleton.number = cls.instances_created
        cls.instances_created += 1
        return cls._singleton

    # __init__方法中除了self之外定义的参数，都将与__new__方法中除cls参数之外的参数是必须保持一致或者等效
    def __init__(self, name='', func=None):
        print("__init__():", self)
        super(Person, self).__init__()
        self.name = name
        self.func = func
        self.count = 0

    def __del__(self):
        print('__del__():', self)
        del self

    def __call__(self, *args, **kwargs):
        self.count += 1
        print('__call__():', self, *args, **kwargs)
        if self.func:
            return self.func(*args, **kwargs)

    # def __repr__(self):
    #     print('__repr__():', self)

    # def __str__(self):
    #     print('__str__():', self)
    #     return self

    def __bytes__(self):
        print('__bytes__():', self)

    def __hash__(self):
        print('__hash__():', self)

    def __bool__(self):
        print('__bool__():', self)

    def __format__(self, format_spec):
        print('__format__():', self, format_spec)


class Child(Person):
    def __new__(cls, *args, **kwargs):
        print('[child]__new__()', cls)
        return Person.__new__(cls, *args, **kwargs)


@Person
def foo():
    pass


for i in range(10):
    foo()

if __name__ == '__main__':
    p = Person('Tom')
    print(p.number, p.name, p.instances_created)
    print(Person.instances_created)
    print(type(p))
    print(callable(p))
    p()

    print('*' * 50)

    c = Child('Jury')
    print(c.number, c.name, c.instances_created)
    print(Child.instances_created)
    print(type(c))

    print('*' * 50)

    print(foo.count)
