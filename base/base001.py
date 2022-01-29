#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# 1 计算器
# 1.1 数字
# print((50 - 5 * 6) / 4)  # division always returns a floating point number
# print(17 / 3)  # classic division returns a float
# print(17 // 3)  # floor division discards the fractional part
# print(17 % 3)  # the % operator returns the remainder of the division
# print(5 * 3 + 2)  # floored quotient * divisor + remainder
# print(5 ** 2)  # 5 squared
# print(4 * 3.75 - 1)  # 混合类型运算数的运算会把整数转换为浮点数

# 1.2 字符串
# print('doesn\'t')  # use \' to escape the single quote...
# print("doesn't")  # # ...or use double quotes instead
# print('"Isn\'t," they said.')  # "Isn't," they said.
# print(r'C:\some\name')  # note the r before the quote
# print("""\
# Usage: thingy [OPTIONS]
#      -h                        Display this usage message
#      -H hostname               Hostname to connect to
# """)  # """...""" 或 '''...'''可以实现跨行连续输入,字符串行尾会自动加上回车换行，如果不需要回车换行，在行尾添加 \ 即可
# print(3 * 'un' + 'ium')  # 字符串可以用 + 合并（粘到一起），也可以用 * 重复
# print('Py' 'thon')  # 相邻的两个或多个 字符串字面值 （引号标注的字符）会自动合并,不能用于变量或表达式
# prefix = 'Py'
# print(prefix + 'thon')  # 合并多个变量，或合并变量与字面值，要用 +
# word = 'Python'
# print(word[0])  # 字符串支持 索引 （下标访问），第一个字符的索引是 0
# print(word[-1])  # 索引还支持负数，用负数索引时，从右边开始计数;注意，-0 和 0 一样，因此，负数索引从 -1 开始
# print(word[0:2])  # 字符串还支持 切片
# print(word[:2])  # 切片索引的默认值很有用；省略开始索引时，默认值为 0
# print(word[4:])  # 省略结束索引时，默认为到字符串的结尾
# print(word[:2] + word[2:])  # 注意，输出结果包含切片开始，但不包含切片结束。因此，s[:i] + s[i:] 总是等于 s
# print(word[4:42])  # 切片会自动处理越界索引
# # word[0] = 'J'  # Python 字符串不能修改，是 immutable 的
# s = 'supercalifragilisticexpialidocious'
# print(len(s))  # 内置函数 len() 返回字符串的长度

# 1.3 列表
# squares = [1, 4, 9, 16, 25]
# print(squares)  # 列表 可以包含不同类型的元素，但一般情况下，各个元素的类型相同
# print(squares[0], squares[-3:])  # 和字符串（及其他内置 sequence 类型）一样，列表也支持索引和切片
# print(squares[:])  # 切片操作返回包含请求元素的新列表。以下切片操作会返回列表的 浅拷贝
# print(squares + [36, 49, 64, 81, 100])  # 列表还支持合并操作
# cubes = [1, 8, 27, 65, 125]
# cubes[3] = 64
# print(cubes)  # 与 immutable 字符串不同, 列表是 mutable 类型，其内容可以改变
# cubes.append(7 ** 3)  # append() 方法 可以在列表结尾添加新元素
# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
# letters[2:5] = ['C', 'D', 'E']  # 为切片赋值可以改变列表大小，甚至清空整个列表
# print(letters)  # ['a', 'b', 'C', 'D', 'E', 'f', 'g']
# letters[2:5] = []
# print(letters)  # ['a', 'b', 'f', 'g']
# letters[:] = []
# print(letters)  # []
# letters = ['a', 'b', 'c', 'd']
# print(len(letters))  # 内置函数 len() 也支持列表
# a = ['a', 'b', 'c']
# n = [1, 2, 3]
# x = [a, n]
# print(x)  # 可以嵌套列表（创建包含其他列表的列表）
# print(x[0], x[0][1])
# a, b = 0, 1
# while a < 10:  # 任何非零整数都为真，零为假；长度非零就为真，空序列则为假
#     print(a, end=',')  # 关键字参数 end 可以取消输出后面的换行, 或用另一个字符串结尾
#     a, b = b, a+b
# print(-3 ** 2)  # -9,** 比 - 的优先级更高

# 2 其他流程控制工具
# 2.1 if
# x = int(input("Please enter an integer: "))
# if x < 0:
#     x = 0
#     print('Negative changed to zero')
# elif x == 0:
#     print('Zero')
# elif x == 1:
#     print('Single')
# else:
#     print('More')

# 2.2 for
# words = ['cat', 'window', 'defenestrate']
# for w in words:
#     print(w, len(w))
# users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}
# for user, status in users.copy().items():
#     if status == 'inactive':
#         del users[user]
# print(users)
# active_users = {}
# for user, status in users.items():
#     if status == 'active':
#         active_users[user] = status
# print(active_users)

# 2.3 range()
# 可迭代对象（iterable）：能够逐一返回其成员项的对象。 可迭代对象的例子包括所有序列类型 (例如 list, str 和 tuple) 以及某些
# 非序列类型例如 dict, 文件对象 以及定义了 __iter__() 方法或是实现了 序列 语义的 __getitem__() 方法的任意自定义类对象。
# 迭代器（iterator）：用来表示一连串数据流的对象。重复调用迭代器的 __next__() 方法（或将其传给内置函数 next()）将逐个返回
# 流中的项。当没有数据可用时则将引发 StopIteration 异常。迭代器必须具有 __iter__() 方法用来返回该迭代器对象自身，因此
# 迭代器必定也是可迭代对象，可被用于其他可迭代对象适用的大部分场合。一个显著的例外是那些会多次重复访问迭代项的代码。
# for i in range(5):
#     print(i)
# print(list(range(5, 10)))  # [5, 6, 7, 8, 9]
# print(list(range(0, 10, 3)))  # [0, 3, 6, 9]
# print(list(range(-10, -100, -30)))  # [-10, -40, -70]
# a = ['Mary', 'had', 'a', 'little', 'lamb']
# for i in range(len(a)):
#     print(i, a[i])
# print(sum(range(4)))  # sum() 是一种把可迭代对象作为参数的函数

# 2.4 循环中的 break、continue 语句及 else 子句
# for n in range(2, 10):
#     for x in range(2, n):
#         if n % x == 0:
#             print(n, 'equals', x, '*', n//x)
#             break
#     else:
#         # loop fell through without finding a factor
#         print(n, 'is a prime number')
# for num in range(2, 10):
#     print("Found an even number", num)
#     continue
#     print("Found an odd number", num)

# 2.5 函数
# def fib(n):    # write Fibonacci series up to n
#     """Print a Fibonacci series up to n."""
#     result = []
#     a, b = 0, 1
#     while a < n:
#         # 调用了列表对象 result 的 方法 。方法是“从属于”对象的函数，命名为 obj.methodname，obj 是对象（也可以是表达式），
#         # methodname 是对象类型定义的方法名
#         result.append(a)
#         a, b = b, a+b
#     return result  # return 语句返回函数的值。return 语句不带表达式参数时，返回 None。函数执行完毕退出也返回 None
# print(fib(2000))

# def ask_ok(prompt, retries=4, reminder='Please try again!'):
#     while True:
#         ok = input(prompt)
#         if ok in ('y', 'ye', 'yes'):
#             return True
#         if ok in ('n', 'no', 'nop', 'nope'):
#             return False
#         retries = retries - 1
#         if retries < 0:
#             raise ValueError('invalid user response')
#         print(reminder)
# ask_ok('Do you really want to quit?')
# ask_ok('OK to overwrite the file?', 2)
# ask_ok('OK to overwrite the file?', 2, 'Come on, only yes or no!')

# i = 5
# def f(arg=i):
#     print(arg)
# i = 6
# f()

# def f(a, L=[]):  # 默认值只计算一次。默认值为列表、字典或类实例等可变对象时，会产生与该规则不同的结果
#     L.append(a)
#     return L
# print(f(1))  # [1]
# print(f(2))  # [1, 2]
# print(f(3))  # [1, 2, 3]

# def f(a, L=None):  # 不想在后续调用之间共享默认值时，应以如下方式编写函数
#     if L is None:
#         L = []
#     L.append(a)
#     return L

# def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):  # 关键字参数
#     print("-- This parrot wouldn't", action, end=' ')
#     print("if you put", voltage, "volts through it.")
#     print("-- Lovely plumage, the", type)
#     print("-- It's", state, "!")
# parrot(1000)                                          # 1 positional argument
# parrot(voltage=1000)                                  # 1 keyword argument
# parrot(voltage=1000000, action='VOOOOOM')             # 2 keyword arguments
# parrot(action='VOOOOOM', voltage=1000000)             # 2 keyword arguments
# parrot('a million', 'bereft of life', 'jump')         # 3 positional arguments
# parrot('a thousand', state='pushing up the daisies')  # 1 positional, 1 keyword
# # parrot()                     # required argument missing
# # parrot(voltage=5.0, 'dead')  # non-keyword argument after a keyword argument
# # parrot(110, voltage=220)     # duplicate value for the same argument
# # parrot(actor='John Cleese')  # unknown keyword argument

# def cheeseshop(kind, *arguments, **keywords):  # 关键字参数在输出结果中的顺序与调用函数时的顺序一致
#     print("-- Do you have any", kind, "?")
#     print("-- I'm sorry, we're all out of", kind)
#     for arg in arguments:
#         print(arg)
#     print("-" * 40)
#     for kw in keywords:
#         print(kw, ":", keywords[kw])
# cheeseshop("Limburger", "It's very runny, sir.",
#            "It's really very, VERY runny, sir.",
#            shopkeeper="Michael Palin",
#            client="John Cleese",
#            sketch="Cheese Shop Sketch")

# def concat(*args, sep="/"):
#     return sep.join(args)
# print(concat("earth", "mars", "venus", sep="."))

# def parrot(voltage, state='a stiff', action='voom'):
#     print("-- This parrot wouldn't", action, end=' ')
#     print("if you put", voltage, "volts through it.", end=' ')
#     print("E's", state, "!")
# d = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"}
# parrot(**d)

# def make_incrementor(n):
#     return lambda x: x + n
# f = make_incrementor(42)
# print(f(1))

# pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
# pairs.sort(key=lambda pair: pair[1])
# print(pairs)

# 文档字符串
# def my_function():
#     """Do nothing, but document it.
#
#     No, really, it doesn't do anything.
#     """
#     pass
# print(my_function.__doc__)

# 函数注解
# def f(ham: str, eggs: str = 'eggs') -> str:
#     print("Annotations:", f.__annotations__)
#     print("Arguments:", ham, eggs)
#     return ham + ' and ' + eggs
# f('spam')

# 3 数据结构
# 3.1 列表详解
# fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
# print(fruits.count('apple'))  # 2
# print(fruits.count('tangerine'))  # 0
# print(fruits.index('banana'))  # 3
# print(fruits.index('banana', 4))  # 6,Find next banana starting a position 4
# fruits.reverse()
# print(fruits)  # ['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange']
# fruits.append('grape')
# print(fruits)  # ['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange', 'grape']
# fruits.sort()  # 不是所有数据都可以排序或比较。例如，[None, 'hello', 10] 就不可排序，因为整数不能与字符串对比，而 None 不能与其他类型对比
# print(fruits)  # ['apple', 'apple', 'banana', 'banana', 'grape', 'kiwi', 'orange', 'pear']
# print(fruits.pop())  # pear
# print(fruits)  # ['apple', 'apple', 'banana', 'banana', 'grape', 'kiwi', 'orange']

# 用列表实现堆栈
# stack = [3, 4, 5]
# stack.append(6)
# stack.append(7)
# print(stack)  # [3, 4, 5, 6, 7]
# print(stack.pop())  # 7
# print(stack)  # [3, 4, 5, 6]

# 用列表实现队列
# from collections import deque
# queue = deque(["Eric", "John", "Michael"])
# queue.append("Terry")
# queue.append("Graham")
# print(queue.popleft())  # Eric
# print(queue.popleft())  # John
# print(queue)  # deque(['Michael', 'Terry', 'Graham'])

# 列表推导式
# squares = list(map(lambda x: x**2, range(10)))
# print(squares)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
# squares = [x**2 for x in range(10)]
# print(squares)
# print([(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y])
# from math import pi
# print([str(round(pi, i)) for i in range(1, 6)])  # ['3.1', '3.14', '3.142', '3.1416', '3.14159']

# 嵌套的列表推导式
# matrix = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12],
# ]
# print([[row[i] for row in matrix] for i in range(4)])  # 转置行列
# print(list(zip(*matrix)))  # 内置函数转置行列

# 3.2 del
# a = [-1, 1, 66.25, 333, 333, 1234.5]
# del a[0]
# print(a)  # [1, 66.25, 333, 333, 1234.5]
# del a[2:4]
# print(a)  # [1, 66.25, 1234.5]
# del a[:]
# print(a)  # [],清空整个列表
# del a  # 再引用 a 就会报错

# 3.3 元组和序列
# t = 12345, 54321, 'hello!'  # 元组输入时，圆括号可有可无，不过经常是必须的（如果元组是更大的表达式的一部分）
# print(t[0])  # v
# print(t)  # (12345, 54321, 'hello!')
# u = t, (1, 2, 3, 4, 5)
# print(u)  # ((12345, 54321, 'hello!'), (1, 2, 3, 4, 5))
# # 元组是 immutable （不可变的），一般可包含异质元素序列，通过解包（见本节下文）或索引访问（如果是 namedtuples，可以属性访问）
# # t[0] = 8888
# x, y, z = t  # 序列解包

# 3.4 集合
# basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
# print(basket)  # {'orange', 'pear', 'banana', 'apple'}
# print('orange' in basket, 'crabgrass' in basket)  # True False
# a = set('abracadabra')
# b = set('alacazam')
# print(a)  # {'c', 'd', 'b', 'a', 'r'}
# print(a - b)  # {'r', 'd', 'b'}
# print(a | b)  # {'c', 'd', 'b', 'l', 'm', 'a', 'r', 'z'}
# print(a & b)  # {'c', 'a'}
# print(a ^ b)  # {'m', 'd', 'b', 'r', 'z', 'l'},不能同时在a、b里
# a = {x for x in 'abracadabra' if x not in 'abc'}  # 集合也支持推导式
# print(a)  # {'r', 'd'}

# 3.5 字典
# tel = {'jack': 4098, 'sape': 4139}
# tel['guido'] = 4127
# print(tel)  # {'jack': 4098, 'sape': 4139, 'guido': 4127}
# print(tel['jack'])  # 4098
# del tel['sape']
# tel['irv'] = 4127
# print(tel)  #{'jack': 4098, 'guido': 4127, 'irv': 4127}
# print(list(tel))   # {'jack': 4098, 'guido': 4127, 'irv': 4127}
# print(sorted(tel))  # ['guido', 'irv', 'jack']
# print('guido' in tel)  # True

# dict() 构造函数可以直接用键值对序列创建字典
# print(dict([('sape', 4139), ('guido', 4127), ('jack', 4098)]))
# 字典推导式可以用任意键值表达式创建字典
# print({x: x ** 2 for x in (2, 4, 6)})
# 关键字是比较简单的字符串时，直接用关键字参数指定键值对更便捷
# print(dict(sape=4139, guido=4127, jack=4098))

# 3.6 循环的技巧
# 在字典中循环时，用 items() 方法可同时取出键和对应的值
# knights = {'gallahad': 'the pure', 'robin': 'the brave'}
# for k, v in knights.items():
#     print(k, v)

# 在序列中循环时，用 enumerate() 函数可以同时取出位置索引和对应的值
# for i, v in enumerate(['tic', 'tac', 'toe']):
#     print(i, v)

# 同时循环两个或多个序列时，用 zip() 函数可以将其内的元素一一匹配
# questions = ['name', 'quest', 'favorite color', 1]
# answers = ['lancelot', 'the holy grail', 'blue']
# print(dict(zip(questions, answers)))
# for q, a in zip(questions, answers):
#     print('What is your {0}?  It is {1}.'.format(q, a))

# 逆向循环序列时，先正向定位序列，然后调用 reversed() 函数
# for i in reversed(range(1, 10, 2)):
#     print(i)

# 按指定顺序循环序列，可以用 sorted() 函数，在不改动原序列的基础上，返回一个重新的序列
# basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
# for i in sorted(basket):
#     print(i)

# 一般来说，在循环中修改列表的内容时，创建新列表比较简单，且安全：
# import math
# raw_data = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]
# print(raw_data)
# filtered_data = []
# for value in raw_data:
#     if not math.isnan(value):
#         filtered_data.append(value)
# print(filtered_data)

# 3.7 深入条件控制
# 布尔运算符 and 和 or 也称为 短路 运算符：其参数从左至右解析，一旦可以确定结果，解析就会停止
# string1, string2, string3 = '', 'Trondheim', 'Hammer Dance'
# non_null = string1 or string2 or string3
# print(non_null)  # Trondheim
# Python 与 C 不同，在表达式内部赋值必须显式使用 海象运算符 :=
# while chunk := fp.read(200):  # 自 Python 3.8 开始
#    print(chunk)

# 3.8 序列和其他类型的比较
# 序列对象可以与相同序列类型的其他对象比较。这种比较使用 字典式 顺序：首先，比较前两个对应元素，如果不相等，则可确定比较结果；
# 如果相等，则比较之后的两个元素，以此类推，直到其中一个序列结束
# 如果两个序列中所有的对应元素都相等，则两个序列相等
# 如果一个序列是另一个的初始子序列，则较短的序列可被视为较小（较少）的序列
# 对于字符串来说，字典式顺序使用 Unicode 码位序号排序单个字符
# print((1, 2, 3) < (1, 2, 4))  # True
# print([1, 2, 3] < [1, 2, 4])  # True
# print('ABC' < 'C' < 'Pascal' < 'Python')  # True
# print((1, 2, 3, 4) < (1, 2, 4))  # True
# print((1, 2) < (1, 2, -1))  # True
# print((1, 2, float('NaN')) < (1, 2, -1))  # False
# print((1, 2, 3) == (1.0, 2.0, 3.0))  # True
# print((1, 2, ('aa', 'ab')) < (1, 2, ('abc', 'a'), 4))  # True
# print(('aa', 'ab') < ('abc', 'a'))  # True

# 4 模块
# 4.1 模块详解
# import fibo.py
# print(fibo.py.fib(1000))
# print(fibo.py.fib2(100))
# print(fibo.py.__name__)
# fib = fibo.py.fib
# print(fib(500))

# (1)直接把模块里的名称导入到另一个模块的符号表
# from fibo.py import fib, fib2
# (2)这种方式会导入所有不以下划线（_）开头的名称。大多数情况下，不要用这个功能，这种方式向解释器导入了一批未知的名称，可能会覆盖已经定义的名称
# from fibo.py import *
# (3)模块名后使用 as 时，直接把 as 后的名称与导入模块绑定
# import fibo.py as fib
# from fibo.py import fib as fibonacci

# 以脚本方式执行模块
# python fibo.py.py <arguments>  # 这项操作将执行模块里的代码，和导入模块一样，但会把 __name__ 赋值为 "__main__"
# if __name__ == "__main__":  # 会把下列代码添加到模块末尾
#     import sys
#     fib(int(sys.argv[1]))
# 导入模块时，不运行这些代码
# 这种操作常用于为模块提供便捷用户接口，或用于测试（把模块当作执行测试套件的脚本运行）
# import fibo.py

# 模块搜索路径
# 导入 spam 模块时，解释器首先查找名为 spam 的内置模块。如果没找到，解释器再从 sys.path 变量中的目录列表里查找 spam.py 文件。
# sys.path 初始化时包含以下位置：
#   输入脚本的目录（或未指定文件时的当前目录）
#   PYTHONPATH （目录列表，与 shell 变量 PATH 的语法一样）
#   The installation-dependent default (by convention including a site-packages directory, handled by the site module)

# “已编译的” Python 文件
# 为了快速加载模块，Python 把模块的编译版缓存在 __pycache__ 目录中，文件名为 module.version.pyc，version 对编译文件格式进行编码，
# 一般是 Python 的版本号
# Python 在两种情况下不检查缓存。其一，从命令行直接载入模块，只重新编译，不存储编译结果；
# 其二，没有源模块，就不会检查缓存。为了支持无源文件（仅编译）发行版本， 编译模块必须在源目录下，并且绝不能有源模块
# 给专业人士的一些小建议：
#   在 Python 命令中使用 -O 或 -OO 开关，可以减小编译模块的大小。-O 去除断言语句，-OO 去除断言语句和 __doc__ 字符串
#   从 .pyc 文件读取的程序不比从 .py 读取的执行速度快，.pyc 文件只是加载速度更快
#   compileall 模块可以为一个目录下的所有模块创建 .pyc 文件

# 4.2 标准模块
# 一个特别值得注意的模块 sys，它被内嵌到每一个 Python 编译器中。sys.ps1 和 sys.ps2 变量定义了一些字符，它们可以用作主提示符和辅助提示符
# import sys
# # print(sys.ps1)  # 终端中运行
# # print(sys.ps2)  # 终端中运行
# sys.path.append('/ufs/guido/lib/python')
# print(sys.path)

# 4.3 dir() 函数
# 内置函数 dir() 用于查找模块定义的名称。返回结果是经过排序的字符串列表
# import fibo.py, sys
# print(dir(fibo.py))
# print(dir(sys))

# 没有参数时，dir() 列出当前定义的名称,该函数列出所有类型的名称：变量、模块、函数等
# a = [1, 2, 3, 4, 5]
# import fibo.py
# fib = fibo.py.fib
# print(dir())

# dir() 不会列出内置函数和变量的名称。这些内容的定义在标准模块 builtins 里
# import builtins
# print(dir(builtins))

# 4.4 包
# 包是一种用“点式模块名”构造 Python 模块命名空间的方法
# 导入包时，Python 搜索 sys.path 里的目录，查找包的子目录
# Python 只把含 __init__.py 文件的目录当成包。这样可以防止以 string 等通用名称命名的目录，无意中屏蔽出现在后方模块搜索路径中的有效模块。
# 最简情况下，__init__.py 只是一个空文件，但该文件也可以执行包的初始化代码，或设置 __all__ 变量
# 还可以从包中导入单个模块，但引用时必须使用子模块的全名
# import sound.effects.echo
# sound.effects.echo.echofilter(input, output, delay=0.7, atten=4)

# 另一种导入子模块的方法
# from sound.effects import echo
# 这段代码还可以加载子模块 echo ，不加包前缀也可以使用。因此，可以按如下方式使用
# echo.echofilter(input, output, delay=0.7, atten=4)

# Import 语句的另一种变体是直接导入所需的函数或变量
# from sound.effects.echo import echofilter
# 同样，这样也会加载子模块 echo，但可以直接使用函数 echofilter()
# echofilter(input, output, delay=0.7, atten=4)

# 使用 from sound.effects import * 时会发生什么？理想情况下，该语句在文件系统查找并导入包的所有子模块。
# 这项操作花费的时间较长，并且导入子模块可能会产生不必要的副作用，这种副作用只有在显式导入子模块时才会发生
# 唯一的解决方案是提供包的显式索引。import 语句使用如下惯例：如果包的 __init__.py 代码定义了列表 __all__，
# 运行 from package import * 时，它就是用于导入的模块名列表。发布包的新版本时，包的作者应更新此列表。
# 如果包的作者认为没有必要在包中执行导入 * 操作，也可以不提供此列表
# 例如，sound/effects/__init__.py 文件包含以下代码：
# __all__ = ["echo", "surround", "reverse"]  # from sound.effects import * 将导入 sound 包中的这三个命名子模块

# 子包参考
# 还可以用 import 语句的 from module import name 形式执行相对导入
# from . import echo
# from .. import formats
# from ..filters import equalizer
# 注意，相对导入基于当前模块名。因为主模块名是 "__main__" ，所以 Python 程序的主模块必须始终使用绝对导入

# 多目录中的包
# 包还支持特殊属性 __path__。该属性初始化为在包的 __init__.py 文件中的代码执行前所在的目录名列表。
# 这个变量可以修改，但这样做会影响将来搜索包中模块和子包的操作

# 实际上，函数定义也是“可执行”的“语句”；执行模块级函数定义时，函数名将被导入到模块的全局符号表。

# 5 输入与输出
# 5.1  更复杂的输出格式
# 两种写入值的方法：表达式语句 和 print() 函数。第三种方法是使用文件对象的 write() 方法；标准输出文件称为 sys.stdout。
# 对输出格式的控制不只是打印空格分隔的值，还需要更多方式。格式化输出包括以下几种方法:

# (1)使用 格式化字符串字面值 ，要在字符串开头的引号/三引号前添加 f 或 F 。在这种字符串中，可以在 { 和 } 字符之间输入引用的变量，
# 或字面值的 Python 表达式
# year = 2016
# event = 'Referendum'
# print(f'Results of the {year} {event}')

# (2)字符串的 str.format() 方法需要更多手动操作。该方法也用 { 和 } 标记替换变量的位置，虽然这种方法支持详细的格式化指令，
# 但需要提供格式化信息
# yes_votes = 42_572_654
# no_votes = 43_132_495
# percentage = yes_votes / (yes_votes + no_votes)
# print('{:-9} YES votes  {:2.2%}'.format(yes_votes, percentage))

# (3)最后，还可以用字符串切片和合并操作完成字符串处理操作，创建任何排版布局。字符串类型还支持将字符串按给定列宽进行填充，这些方法也很有用

# 如果不需要花哨的输出，只想快速显示变量进行调试，可以用 repr() 或 str() 函数把值转化为字符串
# str() 函数返回供人阅读的值，repr() 则生成适于解释器读取的值（如果没有等效的语法，则强制执行 SyntaxError）
# s = 'Hello, world.'
# print(str(s))
# print(repr(s))
# print(str(1 / 7))
# hello = 'hello, world\n'
# hellos = repr(hello)
# print(hellos)

# string 模块包含 Template 类，提供了将值替换为字符串的另一种方法。该类使用 $x 占位符，并用字典的值进行替换，
# 但对格式控制的支持比较有限。
# from string import Template
# s = Template('$who likes $what')
# print(s.substitute(who='tim', what='kung pao'))
# # d = dict(who='tim')
# # print(Template('Give $who $100').substitute(d))

# import math
# print(f'The value of pi is approximately {math.pi:.3f}.')  # 将 pi 舍入到小数点后三位
# table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
# for name, phone in table.items():  # 在 ':' 后传递整数，为该字段设置最小字符宽度，常用于列对齐
#     print(f'{name:10} ==> {phone:10d}')
# animals = 'eels'
# print(f'My hovercraft is full of {animals}.')
# print(f'My hovercraft is full of {animals!r}.')  # '!a' 应用 ascii() ，'!s' 应用 str()，'!r' 应用 repr()

# 花括号及之内的字符（称为格式字段）被替换为传递给 str.format() 方法的对象。
# 花括号中的数字表示传递给 str.format() 方法的对象所在的位置
# print('{0} and {1}'.format('spam', 'eggs'))
# print('{1} and {0}'.format('spam', 'eggs'))

# str.format() 方法中使用关键字参数名引用值
# print('This {food} is {adjective}.'.format(food='spam', adjective='absolutely horrible'))

# 位置参数和关键字参数可以任意组合
# print('The story of {0}, {1}, and {other}.'.format('Bill', 'Manfred', other='Georg'))

# 如果不想分拆较长的格式字符串，最好按名称引用变量进行格式化，不要按位置。
# 这项操作可以通过传递字典，并用方括号 '[]' 访问键来完成
# table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
# print('Jack: {0[Jack]:d}; Sjoerd: {0[Sjoerd]:d}; Dcab: {0[Dcab]:d}'.format(table))

# 也可以用 '**' 符号，把 table 当作传递的关键字参数
# table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
# print('Jack: {Jack:d}; Sjoerd: {Sjoerd:d}; Dcab: {Dcab:d}'.format(**table))

# 与内置函数 vars() 结合使用时，这种方式非常实用，可以返回包含所有局部变量的字典
# for x in range(1, 11):
#     print('{0:2d} {1:3d} {2:4d}'.format(x, x * x, x * x * x))

# 手动格式化字符串
# 字符串对象的 str.rjust() 方法通过在左侧填充空格，对给定宽度字段中的字符串进行右对齐。
# 同类方法还有 str.ljust() 和 str.center()
# for x in range(1, 11):
#     print(repr(x).rjust(2), repr(x * x).rjust(3), end=' ')
#     print(repr(x * x * x).rjust(4))

# 另一种方法是 str.zfill() ，该方法在数字字符串左边填充零，且能识别正负号
# print('12'.zfill(5))
# print('-3.14'.zfill(7))
# print('3.14159265359'.zfill(5))

# 旧式字符串格式化方法
# import math
# print('The value of pi is approximately %5.3f.' % math.pi)

# 5.2 读写文件
# open() 返回 file object，最常用的参数有两个: open(filename, mode)
# 第一个实参是文件名字符串。第二个实参是包含描述文件使用方式字符的字符串。mode 的值包括 'r' ，表示文件只能读取；
# 'w' 表示只能写入（现有同名文件会被覆盖）；'a' 表示打开文件并追加内容，任何写入的数据会自动添加到文件末尾。
# 'r+' 表示打开文件进行读写。mode 实参是可选的，省略时的默认值为 'r'
# f = open('workfile', 'w')

# 在文本模式下读取文件时，默认把平台特定的行结束符（Unix 上为 \n, Windows 上为 \r\n）转换为 \n。在文本模式下写入数据时，
# 默认把 \n 转换回平台特定结束符。这种操作方式在后台修改文件数据对文本文件来说没有问题，
# 但会破坏 JPEG 或 EXE 等二进制文件中的数据。注意，在读写此类文件时，一定要使用二进制模式。

# 在处理文件对象时，最好使用 with 关键字。优点是，子句体结束后，文件会正确关闭，即便触发异常也可以。而且，
# 使用 with 相比等效的 try-finally 代码块要简短得多
# 如果没有使用 with 关键字，则应调用 f.close() 关闭文件，即可释放文件占用的系统资源
# with open('workfile') as f:
#     read_data = f.read()

# f.read(size) 可用于读取文件内容，它会读取一些数据，并返回字符串（文本模式），或字节串对象（在二进制模式下）
# f.readline() 从文件中读取单行数据；字符串末尾保留换行符（\n），只有在文件不以换行符结尾时，文件的最后一行才会省略换行符
# 只要 f.readline() 返回空字符串，就表示已经到达了文件末尾，空行使用 '\n' 表示，该字符串只包含一个换行符
# 从文件中读取多行时，可以用循环遍历整个文件对象
# for line in f:
#     print(line, end='')
# 如需以列表形式读取文件中的所有行，可以用 list(f) 或 f.readlines()

# f.write(string) 把 string 的内容写入文件，并返回写入的字符数
# 写入其他类型的对象前，要先把它们转化为字符串（文本模式）或字节对象（二进制模式）
# f.tell() 返回整数，给出文件对象在文件中的当前位置，表示为二进制模式下时从文件开始的字节数，以及文本模式下的意义不明的数字
# f.seek(offset, whence) 可以改变文件对象的位置。通过向参考点添加 offset 计算位置；参考点由 whence 参数指定。
# whence 值为 0 时，表示从文件开头计算，1 表示使用当前文件位置，2 表示使用文件末尾作为参考点。省略 whence 时，
# 其默认值为 0，即使用文件开头作为参考点
# f = open('workfile', 'rb+')
# f.write(b'0123456789abcdef')
# f.seek(5)      # Go to the 6th byte in the file
# f.read(1)
# f.seek(-3, 2)  # Go to the 3rd byte before the end
# f.read(1)

# 在文本文件（模式字符串未使用 b 时打开的文件）中，只允许相对于文件开头搜索（使用 seek(0, 2) 搜索到文件末尾是个例外），
# 唯一有效的 offset 值是能从 f.tell() 中返回的，或 0。其他 offset 值都会产生未定义的行为

# 使用 json 保存结构化数据
# json 标准模块采用 Python 数据层次结构，并将之转换为字符串表示形式；这个过程称为 serializing （序列化）。
# 从字符串表示中重建数据称为 deserializing （解序化）。
# 在序列化和解序化之间，表示对象的字符串可能已经存储在文件或数据中，或通过网络连接发送到远方 的机器
# import json
# x = [1, 'simple', 'list']
# print(json.dumps(x))  # '[1, "simple", "list"]'

# dumps() 函数还有一个变体， dump() ，它只将对象序列化为 text file。因此，如果 f 是 text file 对象
# json.dump(x, f)

# 要再次解码对象，如果 f 是已打开、供读取的 text file 对象
# x = json.load(f)

# 这种简单的序列化技术可以处理列表和字典，但在 JSON 中序列化任意类的实例，则需要付出额外努力

# 6 错误和异常
# 6.1 句法错误
# 句法错误又称解析错误
# 解析器会复现出现句法错误的代码行，并用小“箭头”指向行里检测到的第一个错误；错误信息还输出文件名与行号
# while True print('Hello world')
# #   File "<stdin>", line 1
# #     while True print('Hello world')
# #                    ^
# # SyntaxError: invalid syntax

# 6.2 异常
# 执行时检测到的错误称为 异常，异常不一定导致严重的后果；大多数异常不会被程序处理，而是显示错误信息
# 错误信息的最后一行说明程序遇到了什么类型的错误。异常有不同的类型，而类型名称会作为错误信息的一部分中打印出来
# print(10 * (1 / 0))
# # Traceback (most recent call last):
# #   File "<stdin>", line 1, in <module>
# #     print(10 * (1 / 0))
# # ZeroDivisionError: division by zero
# print(4 + spam*3)
# # Traceback (most recent call last):
# #   File "<stdin>", line 1, in <module>
# #     print(4 + spam * 3)
# # NameError: name 'spam' is not defined
# print('2' + 2)
# # Traceback (most recent call last):
# #   File "<stdin>", line 1, in <module>
# #     print('2' + 2)
# # TypeError: can only concatenate str (not "int") to str

# 6.3 异常的处理
# try 语句的工作原理如下：
#   - 首先，执行 try 子句 （try 和 except 关键字之间的（多行）语句）
#   - 如果没有触发异常，则跳过 except 子句，try 语句执行完毕
#   - 如果在执行 try 子句时发生了异常，则跳过该子句中剩下的部分。 如果异常的类型与 except 关键字后指定的异常相匹配，
#   则会执行 except 子句，然后跳到 try/except 代码块之后继续执行
#   - 如果发生的异常与 except 子句 中指定的异常不匹配，则它会被传递到外部的 try 语句中；如果没有找到处理程序，
#   则它是一个 未处理异常 且执行将终止并输出如上所示的消息
# while True:
#     try:
#         x = int(input("Please enter a number: "))
#         break
#     except ValueError:
#         print("Oops!  That was no valid number.  Try again...")

# try 语句可以有多个 except 子句 来为不同的异常指定处理程序。 但最多只有一个处理程序会被执行。
# 处理程序只处理对应的 try 子句 中发生的异常，而不处理同一 try 语句内其他处理程序中的异常。
# except 子句 可以用带圆括号的元组来指定多个异常
# try:
#     pass
# except (RuntimeError, TypeError, NameError):
#     pass

# 如果发生的异常与 except 子句中的类是同一个类或是它的基类时，
# 则该类与该异常相兼容（反之则不成立 --- 列出派生类的 except 子句 与基类不兼容）
# 下面的代码将依次打印 B, C, D
# class B(Exception):
#     pass
# class C(B):
#     pass
# class D(C):
#     pass
# for cls in [B, C, D]:
#     try:
#         raise cls()
#     except D:
#         print("D")
#     except C:
#         print("C")
#     except B:
#         print("B")

# 所有异常都继承自 BaseException，因此它可被用作通配符。 但这种用法要非常谨慎小心，因为它很容易掩盖真正的编程错误！
# 它还可被用于打印错误消息然后重新引发异常（允许调用者再来处理该异常）
# import sys
# try:
#     f = open('myfile.txt')
#     s = f.readline()
#     i = int(s.strip())
# except OSError as err:
#     print("OS error: {0}".format(err))
# except ValueError:
#     print("Could not convert data to an integer.")
# except BaseException as err:
#     print(f"Unexpected {err=}, {type(err)=}")
#     raise

# try ... except 语句具有可选的 else 子句，该子句如果存在，它必须放在所有 except 子句 之后。
# 它适用于 try 子句 没有引发异常但又必须要执行的代码
# import sys
# for arg in sys.argv[1:]:
#     try:
#         f = open(arg, 'r')
#     except OSError:
#         print('cannot open', arg)
#     else:
#         print(arg, 'has', len(f.readlines()), 'lines')
#         f.close()

# 发生异常时，它可能具有关联值，即异常 参数 。是否需要参数，以及参数的类型取决于异常的类型
# except 子句 可以在异常名称后面指定一个变量。 这个变量会绑定到一个异常实例并将参数存储在 instance.args 中
# try:
#     raise Exception('spam', 'eggs')
# except Exception as inst:
#     print(type(inst))    # the exception instance
#     print(inst.args)     # arguments stored in .args
#     print(inst)          # __str__ allows args to be printed directly,but may be overridden in exception subclasses
#     x, y = inst.args     # unpack args
#     print('x =', x)      # 如果异常有参数，则它们将作为未处理异常的消息的最后一部分（'详细信息'）打印
#     print('y =', y)

# 异常处理程序不仅会处理在 try 子句 中发生的异常，还会处理在 try 子句 中调用（包括间接调用）的函数
# def this_fails():
#     x = 1/0
# try:
#     this_fails()
# except ZeroDivisionError as err:
#     print('Handling run-time error:', err)

# 6.4 触发异常
# raise 语句支持强制触发指定的异常
# raise NameError('HiThere')
# # Traceback (most recent call last):
# #   File "<stdin>", line 1, in <module>
# #     raise NameError('HiThere')
# # NameError: HiThere

# raise 唯一的参数就是要触发的异常。这个参数必须是异常实例或异常类（派生自 Exception 类）。
# 如果传递的是异常类，将通过调用没有参数的构造函数来隐式实例化
# raise ValueError  # shorthand for 'raise ValueError()'

# 如果只想判断是否触发了异常，但并不打算处理该异常，则可以使用更简单的 raise 语句重新触发异常
# try:
#     raise NameError('HiThere')
# except NameError:
#     print('An exception flew by!')
#     raise

# 6.5 异常链
# raise 语句支持可选的 from 子句，该子句用于启用链式异常
# raise RuntimeError from exc

# 转换异常时，这种方式很有用
# def func():
#     raise ConnectionError
# try:
#     func()
# except ConnectionError as exc:
#     raise RuntimeError('Failed to open database') from exc
# # Traceback (most recent call last):
# #   File "<stdin>", line 2, in <module>
# #     func()
# #   File "<stdin>", line 2, in func
# #     raise ConnectionError
# # ConnectionError
# #
# # The above exception was the direct cause of the following exception:
# #
# # Traceback (most recent call last):
# #   File "<stdin>", line 4, in <module>
# #     raise RuntimeError('Failed to open database') from exc
# # RuntimeError: Failed to open database

# 异常链会在 except 或 finally 子句内部引发异常时自动生成。 这可以通过使用 from None 这样的写法来禁用
# try:
#     open('database.sqlite')
# except OSError:
#     raise RuntimeError from None
# # Traceback (most recent call last):
# #   File "<stdin>", line 4, in <module>
# # RuntimeError

# 6.6 用户自定义异常
# 程序可以通过创建新的异常类命名自己的异常。不论是以直接还是间接的方式，异常都应从 Exception 类派生
# 大多数异常命名都以 “Error” 结尾，类似标准异常的命名
# 许多标准模块都需要自定义异常，以报告由其定义的函数中出现的错误

# 6.7 定义清理操作
# try 语句还有一个可选子句，用于定义在所有情况下都必须要执行的清理操作
# 如果存在 finally 子句，则 finally 子句是 try 语句结束前执行的最后一项任务。
# 不论 try 语句是否触发异常，都会执行 finally 子句。以下内容介绍了几种比较复杂的触发异常情景：
#   - 如果执行 try 子句期间触发了某个异常，则某个 except 子句应处理该异常。如果该异常没有 except 子句处理，
#   在 finally 子句执行后会被重新触发
#   - except 或 else 子句执行期间也会触发异常。 同样，该异常会在 finally 子句执行之后被重新触发
#   - 如果 finally 子句中包含 break、continue 或 return 等语句，异常将不会被重新引发
#   - 如果执行 try 语句时遇到 break,、continue 或 return 语句，
#   则 finally 子句在执行 break、continue 或 return 语句之前执行
#   - 如果 finally 子句中包含 return 语句，则返回值来自 finally 子句的某个 return 语句的返回值，
#   而不是来自 try 子句的 return 语句的返回值
# try:
#     raise KeyboardInterrupt
# finally:
#     print('Goodbye, world!')

# def bool_return():
#     try:
#         return True
#     finally:
#         return False
# print(bool_return())  # False

# def divide(x, y):
#     try:
#         result = x / y
#     except ZeroDivisionError:
#         print("division by zero!")
#     else:
#         print("result is", result)
#     finally:
#         print("executing finally clause")
# # divide(2, 1)
# # divide(2, 0)
# divide("2", "1")

# 6.8 预定义的清理操作
# 某些对象定义了不需要该对象时要执行的标准清理操作。无论使用该对象的操作是否成功，都会执行清理操作
# 这个代码的问题在于，执行完代码后，文件在一段不确定的时间内处于打开状态。在简单脚本中这没有问题，
# 但对于较大的应用程序来说可能会出问题
# for line in open("myfile.txt"):
#     print(line, end="")

# with 语句支持以及时、正确的清理的方式使用文件对象：
# 语句执行完毕后，即使在处理行时遇到问题，都会关闭文件 f。和文件一样，支持预定义清理操作的对象会在文档中指出这一点
# with open("myfile.txt") as f:
#     for line in f:
#         print(line, end="")

# 7 类
# 类把数据与功能绑定在一起。创建新类就是创建新的对象 类型，从而创建该类型的新 实例 。类实例具有多种保持自身状态的属性。
# 类实例还支持（由类定义的）修改自身状态的方法。
# 类继承机制支持多个基类，派生类可以覆盖基类的任何方法，类的方法可以调用基类中相同名称的方法
# 对象可以包含任意数量和类型的数据
# 和模块一样，类也拥有 Python 天然的动态特性：在运行时创建，创建后也可以修改

# 7.1 名称和对象
# 对象之间相互独立，多个名称（在多个作用域内）可以绑定到同一个对象。 其他语言称之为别名。

# 7.2 Python 作用域和命名空间
# namespace （命名空间）是一个从名字到对象的映射;不同命名空间中的名称之间绝对没有关系；
# 例如，两个不同的模块都可以定义一个 maximize 函数而不会产生混淆 --- 模块的用户必须在其前面加上模块名称

# 把任何跟在一个点号之后的名称都称为 属性 --- 例如，在表达式 z.real 中，real 是对象 z 的一个属性。按严格的说法，
# 对模块中名称的引用属于属性引用：在表达式 modname.funcname 中，modname 是一个模块对象而 funcname 是它的一个属性。
# 在此情况下在模块的属性和模块中定义的全局名称之间正好存在一个直观的映射：它们共享相同的命名空间！

# 属性可以是只读或者可写的。如果为后者，那么对属性的赋值是可行的。模块属性是可写的，你可以写 modname.the_answer = 42 。
# 可写的属性同样可以用 del 语句删除。例如， del modname.the_answer 将会从名为 modname 的对象中移除 the_answer 属性

# 命名空间在不同时刻被创建，拥有不同的生存期。包含内置名称的命名空间是在 Python 解释器启动时创建的，永远不会被删除。
# 模块的全局命名空间在模块定义被读入时创建；通常，模块命名空间也会持续到解释器退出。被解释器的顶层调用执行的语句，
# 从一个脚本文件读取或交互式地读取，被认为是 __main__ 模块调用的一部分，因此它们拥有自己的全局命名空间。
# （内置名称实际上也存在于一个模块中；这个模块被称作 builtins 。）

# 一个 作用域 是一个命名空间可直接访问的 Python 程序的文本区域。 这里的 “可直接访问” 意味着对名称的非限定引用会尝试在命名空间中查找名称。
# 虽然作用域是静态地确定的，但它们会被动态地使用。 在执行期间的任何时刻，会有 3 或 4 个命名空间可被直接访问的嵌套作用域:
#   - 最先搜索的最内部作用域包含局部名称
#   - 从最近的封闭作用域开始搜索的任何封闭函数的作用域包含非局部名称，也包括非全局名称
#   - 倒数第二个作用域包含当前模块的全局名称
#   - 最外面的作用域（最后搜索）是包含内置名称的命名空间

# 如果一个名称被声明为全局变量，则所有引用和赋值将直接指向包含该模块的全局名称的中间作用域。 要重新绑定在最内层作用域以外找到的变量，
# 可以使用 nonlocal 语句声明为非本地变量。 如果没有被声明为非本地变量，这些变量将是只读的
# （尝试写入这样的变量只会在最内层作用域中创建一个 新的 局部变量，而同名的外部变量保持不变）。

# 通常，当前局部作用域将（按字面文本）引用当前函数的局部名称。 在函数以外，局部作用域将引用与全局作用域相一致的命名空间：模块的命名空间。
# 类定义将在局部命名空间内再放置另一个命名空间。

# Python 的一个特殊规定是这样的 -- 如果不存在生效的 global 或 nonlocal 语句 -- 则对名称的赋值总是会进入最内层作用域。
# 赋值不会复制数据 --- 它们只是将名称绑定到对象。 删除也是如此：语句 del x 会从局部作用域所引用的命名空间中移除对 x 的绑定。
# 事实上，所有引入新名称的操作都是使用局部作用域：特别地，import 语句和函数定义会在局部作用域中绑定模块或函数名称。

# global 语句可被用来表明特定变量生存于全局作用域并且应当在其中被重新绑定；
# nonlocal 语句表明特定变量生存于外层作用域中并且应当在其中被重新绑定
# def scope_test():
#     def do_local():
#         spam = "local spam"
#     def do_nonlocal():
#         nonlocal spam  # nonlocal 赋值会改变 scope_test 对 spam 的绑定
#         spam = "nonlocal spam"
#     def do_global():
#         global spam  # global 赋值会改变模块层级的绑定
#         spam = "global spam"
#     spam = "test spam"
#     do_local()
#     print("After local assignment:", spam)
#     do_nonlocal()
#     print("After nonlocal assignment:", spam)
#     do_global()
#     print("After global assignment:", spam)
# scope_test()
# print("In global scope:", spam)  # 在 global 赋值之前没有 spam 的绑定

# 7.1 初探类
# 当进入类定义时，将创建一个新的命名空间，并将其用作局部作用域 --- 因此，所有对局部变量的赋值都是在这个新命名空间之内。
# 特别的，函数定义会绑定到这里的新函数名称
# 当（从结尾处）正常离开类定义时，将创建一个 类对象。 这基本上是一个包围在类定义所创建命名空间内容周围的包装器；
# 原始的（在进入类定义之前起作用的）局部作用域将重新生效，类对象将在这里被绑定到类定义头所给出的类名称

# 类对象支持两种操作：属性引用和实例化。
# 属性引用 使用 Python 中所有属性引用所使用的标准语法: obj.name。 有效的属性名称是类对象被创建时存在于类命名空间中的所有名称
# class MyClass:
#     """A simple example class"""
#     i = 12345
#     # 当一个类定义了 __init__() 方法时，类的实例化操作会自动为新创建的类实例发起调用 __init__()
#     # __init__() 方法还可以有额外参数以实现更高灵活性
#     def __init__(self):
#         self.data = []
#     def f(self):
#         return 'hello world'
# # 类的 实例化 使用函数表示法。 可以把类对象视为是返回该类的一个新实例的不带参数的函数
# # 实例化操作（“调用”类对象）会创建一个空对象
# x = MyClass()

# 一般来说，实例变量用于每个实例的唯一数据，而类变量用于类的所有实例共享的属性和方法
# class Dog:
#     # tricks = []  # mistaken use of a class variable
#     kind = 'canine'         # class variable shared by all instances
#     def __init__(self, name):
#         self.name = name    # instance variable unique to each instance
#         self.tricks = []  # creates a new empty list for each dog,正确的类设计应该使用实例变量
#     def add_trick(self, trick):
#         self.tricks.append(trick)
# d = Dog('Fido')
# e = Dog('Buddy')
# # print(d.kind)
# # print(e.kind)
# # print(d.name)
# # print(e.name)
# d.add_trick('roll over')
# e.add_trick('play dead')
# print(d.tricks)  # # unexpectedly shared by all dogs

# 如果同样的属性名称同时出现在实例和类中，则属性查找会优先选择实例
# class Warehouse:
#     purpose = 'storage'
#     region = 'west'
# w1 = Warehouse()
# print(w1.purpose, w1.region)
# w2 = Warehouse()
# w2.region = 'east'
# print(w2.purpose, w2.region)  # storage east

# def f1(self, x, y):
#     return min(x, x+y)
# class C:
#     f = f1
#     def g(self):
#         return 'hello world'
#     h = g

# 派生类定义的执行过程与基类相同。 当构造类对象时，基类会被记住。 此信息将被用来解析属性引用：
# 如果请求的属性在类中找不到，搜索将转往基类中进行查找。 如果基类本身也派生自其他某个类，则此规则将被递归地应用。
# class DerivedClassName(modname.BaseClassName):

# Python有两个内置函数可被用于继承机制：
#   - 使用 isinstance() 来检查一个实例的类型: isinstance(obj, int) 仅会在 obj.__class__ 为 int
#   或某个派生自 int 的类时为 True
#   - 使用 issubclass() 来检查类的继承关系: issubclass(bool, int) 为 True，因为 bool 是 int 的子类。
#   但是，issubclass(float, int) 为 False，因为 float 不是 int 的子类

# 多重继承
# 搜索从父类所继承属性的操作是深度优先、从左至右的，当层次结构中存在重叠时不会在同一个类中搜索两次。
# 因此，如果某一属性在 DerivedClassName 中未找到，则会到 Base1 中搜索它，然后（递归地）到 Base1 的基类中搜索，
# 如果在那里未找到，再到 Base2 中搜索，依此类推
# 真实情况比这个更复杂一些；方法解析顺序会动态改变以支持对 super() 的协同调用
# 因为所有多重继承的情况都会显示出一个或更多的菱形关联（即至少有一个父类可通过多条路径被最底层类所访问）。 例如，所有类都是继承自 object
# class DerivedClassName(Base1, Base2, Base3):

# 私有变量
# 那种仅限从一个对象内部访问的“私有”实例变量在 Python 中并不存在。 但是，大多数 Python 代码都遵循这样一个约定：
# 带有一个下划线的名称 (例如 _spam) 应该被当作是 API 的非公有部分 (无论它是函数、方法或是数据成员)。
# 由于存在对于类私有成员的有效使用场景（例如避免名称与子类所定义的名称相冲突），因此存在对此种机制的有限支持，称为 名称改写。
# 任何形式为 __spam 的标识符（至少带有两个前缀下划线，至多一个后缀下划线）的文本将被替换为 _classname__spam，
# 其中 classname 为去除了前缀下划线的当前类名称。 这种改写不考虑标识符的句法位置，只要它出现在类定义内部就会进行。
# 名称改写有助于让子类重载方法而不破坏类内方法调用
# class Mapping:
#     def __init__(self, iterable):
#         self.items_list = []
#         self.__update(iterable)
#     def update(self, iterable):
#         for item in iterable:
#             self.items_list.append(item)
#     __update = update   # private copy of original update() method,在 Mapping 类中被替换为 _Mapping__update
# class MappingSubclass(Mapping):
#     def update(self, keys, values):  # 在 MappingSubclass 类中被替换为 _MappingSubclass__update
#         # provides new signature for update()
#         # but does not break __init__()
#         for item in zip(keys, values):
#             self.items_list.append(item)

# 请注意传递给 exec() 或 eval() 的代码不会将发起调用类的类名视作当前类；这类似于 global 语句的效果，
# 因此这种效果仅限于同时经过字节码编译的代码。 同样的限制也适用于 getattr(), setattr() 和 delattr()，
# 以及对于 __dict__ 的直接引用

# 迭代器
# for 语句会在容器对象上调用 iter()。 该函数返回一个定义了 __next__() 方法的迭代器对象，此方法将逐一访问容器中的元素。
# 当元素用尽时，__next__() 将引发 StopIteration 异常来通知终止 for 循环
# s = 'abc'
# it = iter(s)
# print(it)
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))

# 定义一个 __iter__() 方法来返回一个带有 __next__() 方法的对象。
# 如果类已定义了 __next__()，则 __iter__() 可以简单地返回 self
# class Reverse:
#     """Iterator for looping over a sequence backwards."""
#     def __init__(self, data):
#         self.data = data
#         self.index = len(data)
#     def __iter__(self):
#         return self
#     def __next__(self):
#         if self.index == 0:
#             raise StopIteration
#         self.index = self.index - 1
#         return self.data[self.index]
# rev = Reverse('spam')
# print(iter(rev))
# for char in rev:
#     print(char)

# 生成器
# 生成器 是一个用于创建迭代器的简单而强大的工具。
# 它们的写法类似于标准的函数，但当它们要返回数据时会使用 yield 语句。
# 每次在生成器上调用 next() 时，它会从上次离开的位置恢复执行（它会记住上次执行语句时的所有数据值）
# def reverse(data):
#     for index in range(len(data)-1, -1, -1):
#         # 另一个关键特性在于局部变量和执行状态会在每次调用之间自动保存。 这使得该函数
#         # 相比使用 self.index 和 self.data 这种实例变量的方式更易编写且更为清晰
#         yield data[index]  # 生成器的写法更为紧凑，因为它会自动创建 __iter__() 和 __next__() 方法
# for char in reverse('golf'):
#     print(char)

# 生成器表达式
# 某些简单的生成器可以写成简洁的表达式代码，所用语法类似列表推导式，但外层为圆括号而非方括号。
# 这种表达式被设计用于生成器将立即被外层函数所使用的情况。
# 生成器表达式相比完整的生成器更紧凑但较不灵活，相比等效的列表推导式则更为节省内存。
# print(sum(i * i for i in range(10)))
# xvec = [10, 20, 30]
# yvec = [7, 5, 3]
# print(sum(x * y for x, y in zip(xvec, yvec)))
# # unique_words = set(word for line in page for word in line.split())
# # valedictorian = max((student.gpa, student.name) for student in graduates)
# data = 'golf'
# print(list(data[i] for i in range(len(data) - 1, -1, -1)))

# 8 标准库简介
# 8.1 操作系统接口
# import os
# print(os.getcwd())
# # print(os.chdir('/server/accesslogs'))
# print(os.system('mkdir today'))
# print(dir(os))
# print(help(os))

# import shutil  # 对于日常文件和目录管理任务， shutil 模块提供了更易于使用的更高级别的接口
# shutil.copyfile('fibo.py', 'fibo.py.bak')
# shutil.move('fibo.py.bak', 'abc/fibo.py')

# 8.2 文件通配符
# import glob  # glob 模块提供了一个在目录中使用通配符搜索创建文件列表的函数
# print(glob.glob('*.py'))

# 8.3 命令行参数
# import sys  # 通用实用程序脚本通常需要处理命令行参数。这些参数作为列表存储在 sys 模块的 argv 属性中
# print(sys.argv)
# import argparse  # argparse 模块提供了一种更复杂的机制来处理命令行参数
# # 当在通过 python top.py --lines=5 alpha.txt beta.txt 在命令行运行时，
# # 该脚本会将 args.lines 设为 5 并将 args.filenames 设为 ['alpha.txt', 'beta.txt']
# parser = argparse.ArgumentParser(prog='top', description='Show top lines from each file')
# parser.add_argument('filenames', nargs='+')
# parser.add_argument('-l', '--lines', type=int, default=10)
# args = parser.parse_args()
# print(args)

# 8.4 错误输出重定向和程序终止
# sys 模块还具有 stdin ， stdout 和 stderr 的属性。后者对于发出警告和错误消息非常有用，即使在 stdout 被重定向后也可以看到它们
# 终止脚本的最直接方法是使用 sys.exit()
# import sys
# sys.stderr.write('Warning, log file not found starting a new one\n')

# 8.5 字符串模式匹配
# import re
# print(re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest'))  # ['foot', 'fell', 'fastest']
# print(re.sub(r'(\b[a-z]+) \1', r'\1', 'cat in the the hat'))  # cat in the hat
# print('tea for too'.replace('too', 'two'))  # tea for two

# 8.6 数学
# import math  # math 模块提供对浮点数学的底层C库函数的访问
# print(math.cos(math.pi / 4))
# print(math.log(1024, 2))

# import random  # random 模块提供了进行随机选择的工具
# print(random.choice(['apple', 'pear', 'banana']))
# print(random.sample(range(100), 10))  # sampling without replacement
# print(random.random())  # random float
# print(random.randrange(6))  # random integer chosen from range(6)

# import statistics  # statistics 模块计算数值数据的基本统计属性（均值，中位数，方差等）
# data = [2.75, 1.75, 1.25, 0.25, 0.5, 1.25, 3.5]
# print(statistics.mean(data))
# print(statistics.median(data))
# print(statistics.variance(data))

# 8.7 互联网访问
# from urllib.request import urlopen
# with urlopen('http://worldtimeapi.org/api/timezone/etc/UTC.txt') as response:
#     for line in response:
#         line = line.decode()             # Convert bytes to a str
#         if line.startswith('datetime'):
#             print(line.rstrip())  # # Remove trailing newline
#  import smtplib
# server = smtplib.SMTP('localhost')
# server.sendmail('soothsayer@example.org', 'jcaesar@example.org')
# server.quit()

# 8.8 日期和时间
# datetime 模块提供了以简单和复杂的方式操作日期和时间的类。
# 虽然支持日期和时间算法，但实现的重点是有效的成员提取以进行输出格式化和操作。该模块还支持可感知时区的对象
# from datetime import date
# now = date.today()
# print(now)
# print(now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B."))
# birthday = date(1964, 7, 31)
# age = now - birthday
# print(age.days)

# 8.9 数据压缩
# 常见的数据存档和压缩格式由模块直接支持，包括：zlib, gzip, bz2, lzma, zipfile 和 tarfile
# import zlib
# s = b'witch which has which witches wrist watch'
# print(len(s))
# t = zlib.compress(s)
# print(len(t))
# print(zlib.decompress(t))
# print(zlib.crc32(s))

# 8.10 性能测量
# 与 timeit 的精细粒度级别相反， profile 和 pstats 模块提供了用于在较大的代码块中识别时间关键部分的工具
# from timeit import Timer
# print(Timer('t=a; a=b; b=t', 'a=1; b=2').timeit())
# print(Timer('a,b = b,a', 'a=1; b=2').timeit())

# 8.11 质量控制
# doctest 模块提供了一个工具，用于扫描模块并验证程序文档字符串中嵌入的测试
# def average(values):
#     """Computes the arithmetic mean of a list of numbers.
#     >>> print(average([20, 30, 70]))
#     40.0
#     """
#     return sum(values) / len(values)
# import doctest
# doctest.testmod()

# unittest 模块不像 doctest 模块那样易于使用，但它允许在一个单独的文件中维护更全面的测试集
# import unittest
# def average(values):
#     return sum(values) / len(values)
# class TestStatisticalFunctions(unittest.TestCase):
#     def test_average(self):
#         self.assertEqual(average([20, 30, 70]), 40.0)
#         self.assertEqual(round(average([1, 5, 7]), 1), 4.3)
#         with self.assertRaises(ZeroDivisionError):
#             average([])
#         with self.assertRaises(TypeError):
#             average(20, 30, 70)
# unittest.main()  # Calling from the command line invokes all tests

# 自带电池
# - xmlrpc.client 和 xmlrpc.server 模块使得实现远程过程调用变成了小菜一碟。 尽管存在于模块名称中，
# 但用户不需要直接了解或处理 XML
# -  email 包是一个用于管理电子邮件的库，包括MIME和其他符合 RFC 2822 规范的邮件文档。
# 与 smtplib 和 poplib 不同（它们实际上做的是发送和接收消息），电子邮件包提供完整的工具集，
# 用于构建或解码复杂的消息结构（包括附件）以及实现互联网编码和标头协议
# -  json 包为解析这种流行的数据交换格式提供了强大的支持。 csv 模块支持以逗号分隔值格式直接读取和写入文件，
# 这种格式通常为数据库和电子表格所支持。 XML 处理由 xml.etree.ElementTree ， xml.dom 和 xml.sax 包支持。
# 这些模块和软件包共同大大简化了 Python 应用程序和其他工具之间的数据交换
# -  sqlite3 模块是 SQLite 数据库库的包装器，提供了一个可以使用稍微非标准的 SQL 语法更新和访问的持久数据库
# - 国际化由许多模块支持，包括 gettext ， locale ，以及 codecs 包

# 9 标准库简介 —— 第二部分
# 9.1 格式化输出
# reprlib 模块提供了一个定制化版本的 repr() 函数，用于缩略显示大型或深层嵌套的容器对象
# import reprlib
# print(reprlib.repr(set('supercalifragilisticexpialidocious')))

# pprint 模块提供了更加复杂的打印控制，其输出的内置对象和用户自定义对象能够被解释器直接读取。
# 当输出结果过长而需要折行时，“美化输出机制”会添加换行符和缩进，以更清楚地展示数据结构
# import pprint
# t = [[[['black', 'cyan'], 'white', ['green', 'red']], [['magenta', 'yellow'], 'blue']]]
# pprint.pprint(t, width=30)

# textwrap 模块能够格式化文本段落，以适应给定的屏幕宽度
# import textwrap
# doc = """The wrap() method is just like fill() except that it returns
# a list of strings instead of one big string with newlines to separate
# the wrapped lines."""
# print(textwrap.fill(doc, width=40))

# locale 模块处理与特定地域文化相关的数据格式。
# locale 模块的 format 函数包含一个 grouping 属性，可直接将数字格式化为带有组分隔符的样式
# import locale
# print(locale.setlocale(locale.LC_ALL, 'English_United States.1252'))
# conv = locale.localeconv()
# x = 1234567.8
# print(locale.format_string("%d", x, grouping=True))
# print(locale.format_string("%s%.*f", (conv['currency_symbol'], conv['frac_digits'], x), grouping=True))
# print((conv['currency_symbol'], conv['frac_digits'], x))

# 9.2 模板
# string 模块包含一个通用的 Template 类，具有适用于最终用户的简化语法。它允许用户在不更改应用逻辑的情况下定制自己的应用
# t = Template('${village}folk send $$10 to $cause.')
# print(t.substitute(village='Nottingham', cause='the ditch fund'))

# 如果在字典或关键字参数中未提供某个占位符的值，那么 substitute() 方法将抛出 KeyError。
# 对于邮件合并类型的应用，用户提供的数据有可能是不完整的，此时使用 safe_substitute() 方法更加合适 ——
# 如果数据缺失，它会直接将占位符原样保留
# from string import Template
# t = Template('Return the $item to $owner.')
# d = dict(item='unladen swallow')
# # print(t.substitute(d))
# print(t.safe_substitute(d))

# Template 的子类可以自定义分隔符。例如，以下是某个照片浏览器的批量重命名功能，采用了百分号作为日期、照片序号和照片格式的占位符
# from string import Template
# import time, os.path
# from string import Template
# photofiles = ['img_1074.jpg', 'img_1076.jpg', 'img_1077.jpg']
# class BatchRename(Template):
#     delimiter = '%'
# fmt = input('Enter rename style (%d-date %n-seqnum %f-format):  ')  # Ashley_%n%f
# t = BatchRename(fmt)
# date = time.strftime('%d%b%y')
# for i, filename in enumerate(photofiles):
#     base, ext = os.path.splitext(filename)
#     print((base, ext))
#     newname = t.substitute(d=date, n=i, f=ext)
#     print('{0} --> {1}'.format(filename, newname))

# 9.3 使用二进制数据记录格式
# struct 模块提供了 pack() 和 unpack() 函数，用于处理不定长度的二进制记录格式。
# 下面的例子展示了在不使用 zipfile 模块的情况下，如何循环遍历一个 ZIP 文件的所有头信息。
# Pack 代码 "H" 和 "I" 分别代表两字节和四字节无符号整数。"<" 代表它们是标准尺寸的小端字节序
# import struct
# with open('myfile.zip', 'rb') as f:
#     data = f.read()
# start = 0
# for i in range(3):                      # show the first 3 file headers
#     start += 14
#     fields = struct.unpack('<IIIHH', data[start:start+16])
#     crc32, comp_size, uncomp_size, filenamesize, extra_size = fields
#     start += 16
#     filename = data[start:start+filenamesize]
#     start += filenamesize
#     extra = data[start:start+extra_size]
#     print(filename, hex(crc32), comp_size, uncomp_size)
#     start += extra_size + comp_size     # skip to the next header

# 9.4 多线程
# 线程是一种对于非顺序依赖的多个任务进行解耦的技术。多线程可以提高应用的响应效率，
# 当接收用户输入的同时，保持其他任务在后台运行。一个有关的应用场景是，将 I/O 和计算运行在两个并行的线程中
# import threading, zipfile
# class AsyncZip(threading.Thread):
#     def __init__(self, infile, outfile):
#         threading.Thread.__init__(self)
#         self.infile = infile
#         self.outfile = outfile
#     def run(self):
#         f = zipfile.ZipFile(self.outfile, 'w', zipfile.ZIP_DEFLATED)
#         f.write(self.infile)
#         f.close()
#         print('Finished background zip of:', self.infile)
# background = AsyncZip('mydata.txt', 'myarchive.zip')
# background.start()
# print('The main program continues to run in foreground.')
# background.join()    # Wait for the background task to finish
# print('Main program waited until background was done.')

# 多线程应用面临的主要挑战是，相互协调的多个线程之间需要共享数据或其他资源。
# 为此，threading 模块提供了多个同步操作原语，包括线程锁、事件、条件变量和信号量

# 尽管这些工具非常强大，但微小的设计错误却可以导致一些难以复现的问题。因此，实现多任务协作的首选方法是将所有对资源的请求
# 集中到一个线程中，然后使用 queue 模块向该线程供应来自其他线程的请求。 应用程序使用 Queue 对象进行线程间通信和协调，
# 更易于设计，更易读，更可靠

# 9.5 日志记录
# logging 模块提供功能齐全且灵活的日志记录系统。在最简单的情况下，日志消息被发送到文件或 sys.stderr
# 默认情况下，informational 和 debugging 消息被压制，输出会发送到标准错误流。其他输出选项包括将消息转发到电子邮件，
# 数据报，套接字或 HTTP 服务器。新的过滤器可以根据消息优先级选择不同的路由方式：DEBUG，INFO，WARNING，ERROR，和 CRITICAL
# 日志系统可以直接从 Python 配置，也可以从用户配置文件加载，以便自定义日志记录而无需更改应用程序
# import logging
# logging.debug('Debugging information')
# logging.info('Informational message')
# logging.warning('Warning:config file %s not found', 'server.conf')
# logging.error('Error occurred')
# logging.critical('Critical error -- shutting down')

# 9.6 弱引用
# Python 会自动进行内存管理（对大多数对象进行引用计数并使用 garbage collection 来清除循环引用）。
# 当某个对象的最后一个引用被移除后不久就会释放其所占用的内存
# weakref 模块提供的工具可以不必创建引用就能跟踪对象。 当对象不再需要时，它将自动从一个弱引用表中被移除，
# 并为弱引用对象触发一个回调。 典型应用包括对创建开销较大的对象进行缓存
# import weakref, gc
# class A:
#     def __init__(self, value):
#         self.value = value
#     def __repr__(self):
#         return str(self.value)
# a = A(10)                   # create a reference
# d = weakref.WeakValueDictionary()
# d['primary'] = a            # does not create a reference
# print(d['primary'])         # fetch the object if it is still alive
# del a                       # remove the one reference
# print(gc.collect())         # run garbage collection right away
# # print(d['primary'])         # entry was automatically removed

# 9.7 用于操作列表的工具
# array 模块提供了一种 array() 对象，它类似于列表，但只能存储类型一致的数据且存储密集更高
# from array import array
# a = array('H', [4000, 10, 700, 22222])
# print(sum(a))  # 26932
# print(a[1:3])  # array('H', [10, 700])

# collections 模块提供了一种 deque() 对象，它类似于列表，但从左端添加和弹出的速度较快，
# 而在中间查找的速度较慢。 此种对象适用于实现队列和广度优先树搜索
# from collections import deque
# d = deque(["task1", "task2", "task3"])
# d.append("task4")
# print("Handling", d.popleft())

# unsearched = deque([starting_node])
# def breadth_first_search(unsearched):
#     node = unsearched.popleft()
#     for m in gen_moves(node):
#         if is_goal(m):
#             return m
#         unsearched.append(m)

# 在替代的列表实现以外，标准库也提供了其他工具，例如 bisect 模块具有用于操作有序列表的函数
# import bisect
# scores = [(100, 'perl'), (200, 'tcl'), (400, 'lua'), (500, 'python')]
# bisect.insort(scores, (300, 'ruby'))
# print(scores)

# heapq 模块提供了基于常规列表来实现堆的函数。 最小值的条目总是保持在位置零。
# 这对于需要重复访问最小元素而不希望运行完整列表排序的应用来说非常有用
# from heapq import heapify, heappop, heappush
# data = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
# print(heapify(data))  # rearrange the list into heap order
# print(data)  # [0, 1, 2, 6, 3, 5, 4, 7, 8, 9]
# print(heappush(data, -5))  # add a new entry
# print(data)  # [-5, 0, 2, 6, 1, 5, 4, 7, 8, 9, 3]
# print([heappop(data) for i in range(3)])  # fetch the three smallest entries
# print(data)  # [2, 3, 4, 6, 9, 5, 8, 7]

# 9.8 十进制浮点运算
# decimal 模块提供了一种 Decimal 数据类型用于十进制浮点运算。 相比内置的 float 二进制浮点实现，该类特别适用于：
#   - 财务应用和其他需要精确十进制表示的用途，
#   - 控制精度，
#   - 控制四舍五入以满足法律或监管要求，
#   - 跟踪有效小数位，或
#   - 用户期望结果与手工完成的计算相匹配的应用程序
# from decimal import *
# print(round(Decimal('0.70') * Decimal('1.05'), 2))
# print(round(.70 * 1.05, 2))

# Decimal 表示的结果会保留尾部的零，并根据具有两个有效位的被乘数自动推出四个有效位。
# Decimal 可以模拟手工运算来避免当二进制浮点数无法精确表示十进制数时会导致的问题
# 精确表示特性使得 Decimal 类能够执行对于二进制浮点数来说不适用的模运算和相等性检测
# decimal 模块提供了运算所需要的足够精度
# from decimal import *
# print(Decimal('1.00') % Decimal('.10'))  # 0.00
# print(1.00 % 0.10)  # 0.09999999999999995
# print(sum([Decimal('0.1')] * 10) == Decimal('1.0'))  #True
# print(sum([0.1] * 10) == 1.0)  # False
# getcontext().prec = 36
# print(Decimal(1) / Decimal(7))  #Decimal('0.142857142857142857142857142857142857')

# 10 虚拟环境和包
# 10.1 概述
# Python应用程序通常会使用不在标准库内的软件包和模块。应用程序有时需要特定版本的库，因为应用程序可能需要修复特定的错误，
# 或者可以使用库的过时版本的接口编写应用程序。
# 这个问题的解决方案是创建一个 virtual environment，一个目录树，其中安装有特定Python版本，以及许多其他包
# 创建虚拟环境
# 用于创建和管理虚拟环境的模块称为 venv。venv 通常会安装你可用的最新版本的 Python。如果您的系统上有多个版本的 Python，
# 您可以通过运行 python3 或您想要的任何版本来选择特定的Python版本

# 10.2 创建虚拟环境
# 要创建虚拟环境，请确定要放置它的目录，并将 venv 模块作为脚本运行目录路径
# 创建 tutorial-env 目录，如果它不存在的话，并在其中创建包含 Python 解释器副本和各种支持文件的目录
# 虚拟环境的常用目录位置是 .venv。 这个名称通常会令该目录在你的终端中保持隐藏，从而避免需要对所在目录进行额外解释的一般名称。
# 它还能防止与某些工具所支持的 .env 环境变量定义文件发生冲突
# python3 -m venv tutorial-env

# 创建虚拟环境后，您可以激活它
# tutorial-env\Scripts\activate.bat  # 在Windows上，运行
# source tutorial-env/bin/activate  # 在Unix或MacOS上，运行

# 10.3 使用pip管理包
# 默认情况下 pip 将从 Python Package Index <https://pypi.org> 安装软件包
# pip 有许多子命令: "install", "uninstall", "freeze" 等等
# (tutorial-env) $ python -m pip install requests==2.6.0  # 包名称后跟 == 和版本号来安装特定版本的包
# (tutorial-env) $ pip show requests  # 显示有关特定包的信息
# (tutorial-env) $ pip list  # 显示虚拟环境中安装的所有软件包
# (tutorial-env) $ pip freeze > requirements.txt  # 生成一个类似的已安装包列表
# (tutorial-env) $ python -m pip install -r requirements.txt  # 用户可以使用 install -r 安装所有必需的包

# 其他
# import site
# print(site.getusersitepackages())

# import os
# filename = os.environ.get('PYTHONSTARTUP')
# if filename and os.path.isfile(filename):
#     with open(filename) as fobj:
#         startup_file = fobj.read()
#     exec(startup_file)

#!/usr/bin/env python3.5









































