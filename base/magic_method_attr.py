#!/usr/bin/env python
# -*- coding: UTF-8 -*-
class AttrMethod:
    count = 0

    def __init__(self, name, age):
        self.name = name
        print(self.__dict__)
        self.age = age
        print(self.__dict__)

    # def __setattr__(self, key, value):
    #     print("*" * 50)
    #     print("setting:{},  with:{}".format(key, value))
    #     print("current __dict__ : {}".format(self.__dict__))
    #     self.__dict__[key] = value

    # def __getattr__(self, item):
    #     if item in self.__dict__:
    #         return self[item]
    #     return None

    # def __getattribute__(self, item):
    #     print("开始属性校验拦截功能")
    #     print(item)
    #     if item == "name":
    #         print("现在开始调用的是name属性")
    #     elif item == "age":
    #         print("现在开始调用的是age属性")
    #     else:
    #         print("现在开始调用的是其他属性")
    #     return super(AttrMethod, self).__getattribute__(item)

    # def my_set(self, aa, bb):
    #     x = aa
    #     aa = bb
    #     bb = x
    #     print("aa: %s, bb: %s" % (aa, bb))

    def __dir__(self):
        return self.__dict__

    def __get__(self, instance, owner):
        print("__get__")

    def __set__(self, instance, value):
        print("__set__")

    def __delattr__(self, item):
        print("__delattr__")

    def __delete__(self, instance):
        print("__delete__")


if __name__ == '__main__':
    a = AttrMethod('Jojo', '18')
    print("*" * 50)
    print(a.name)
    # print(a.sex)

    # setattr(a, 'asf', {'a': 1})
    # print(a.asf)

    print(dir(a))

    # print("*" * 50)
    # print(a.__dict__)
    # c = getattr(a, 'my_set')
    # c('1', '2')

    # setattr(a, 'name', 'bin')
    # print(getattr(a, 'name'))
