#!/usr/bin/env python
# -*- coding: UTF-8 -*-
class Person(object):
    def __new__(cls, *args, **kwargs):
        print('__new__')

    def __init__(self, name):
        print('__init__')
        self.name = name

    def __del__(self):
        print('__del__')

    def __call__(self, *args, **kwargs):
        print('__call__')

    def __repr__(self):
        print('__repr__')

    def __str__(self):
        print('__str__')

    def __bytes__(self):
        print('__bytes__')

    def __hash__(self):
        print('__hash__')

    def __bool__(self):
        print('__bool__')

    def __format__(self, format_spec):
        print('__format__')


if __name__ == '__main__':
    p = Person('Tom')
    del p
    print(19 / 4)
    print(4.75 * 4)