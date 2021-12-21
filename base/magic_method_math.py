#!/usr/bin/env python
# -*- coding: UTF-8 -*-
class MathMethod:
    def __init__(self, num):
        self.num = num

    def __add__(self, other):
        return self.num + other

    def __sub__(self, other):
        return self.num - other

    def __mul__(self, other):
        return self.num * other

    def __truediv__(self, other):
        return self.num / other

    def __floordiv__(self, other):
        return self.num / other

    def __mod__(self, other):
        return self.num % other

    def __divmod__(self, other):
        return self.num % other

    def __pow__(self, power, modulo=None):
        return self.num ** power

    def __lshift__(self, other):
        return self.num << other

    def __rshift__(self, other):
        return self.num >> other

    def __and__(self, other):
        return self.num & other

    def __xor__(self, other):
        return self.num ^ other

    def __or__(self, other):
        return self.num | other


if __name__ == '__main__':
    a = MathMethod(12)
    print("a + 3 = {}".format(a + 3))
    print("a - 3 = {}".format(a - 3))
    print("a * 3 = {}".format(a * 3))
    print("a / 3 = {}".format(a / 3))
    print("a % 3 = {}".format(a % 3))
    print("a ** 3 = {}".format(a ** 3))
    print("a << 3 = {}".format(a << 3))
    print("a >> 3 = {}".format(a >> 3))
    print("a & 3 = {}".format(a & 3))
    print("a ^ 3 = {}".format(a ^ 3))
    print("a | 3 = {}".format(a | 3))

