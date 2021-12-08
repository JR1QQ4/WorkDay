#!/usr/bin/env python
# -*- coding: UTF-8 -*-
class CompareMethod:
    def __init__(self, num):
        self.num = num

    def __lt__(self, other):
        return self.num < other

    def __le__(self, other):
        return self.num <= other

    def __eq__(self, other):
        return self.num == other

    def __ne__(self, other):
        return self.num != other

    def __gt__(self, other):
        return self.num > other

    def __ge__(self, other):
        return self.num >= other


if __name__ == '__main__':
    n = CompareMethod(10)
    print("n <  20? {}".format(n < 20))
    print("n <= 20? {}".format(n <= 20))
    print("n == 20? {}".format(n == 20))
    print("n != 20? {}".format(n != 20))
    print("n >  20? {}".format(n > 20))
    print("n >= 20? {}".format(n >= 20))

