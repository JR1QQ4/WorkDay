#!/usr/bin/env python
# -*- coding: UTF-8 -*-
class MathMethod:
    def __init__(self, num):
        self.num = num

    def __add__(self, other):
        return self.num + other
