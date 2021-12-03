#!/usr/bin/env python
# -*- coding: UTF-8 -*-
class AttrMethod:
    count = 0

    def __init__(self, name, age):
        self.name = name
        print(self.__dict__)
        self.age = age
        print(self.__dict__)

    def __setattr__(self, key, value):
        print("*" * 50)
        print("setting:{},  with:{}".format(key, value))
        print("current __dict__ : {}".format(self.__dict__))
        self.__dict__[key] = value

    def __getattr__(self, item):
        if item in self.__dict__:
            return self[item]
        return None

    def set(self, aa, bb):
        x = aa
        aa = bb
        bb = x
        print("aa: %s, bb: %s" % (aa, bb))


if __name__ == '__main__':
    a = AttrMethod('Jojo', '18')
    print("*" * 50)
    print(a.name)
    print(a.sex)

    setattr(a, 'asf', {'a': 1})
    print(a.asf)

    print("*" * 50)
    print(a.__dict__)
    c = getattr(a, 'set')
    c('1', '2')

    # setattr(a, 'name', 'bin')
    # print(getattr(a, 'name'))
