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
# import fibo
# print(fibo.fib(1000))
# print(fibo.fib2(100))
# print(fibo.__name__)
# fib = fibo.fib
# print(fib(500))

# (1)直接把模块里的名称导入到另一个模块的符号表
# from fibo import fib, fib2
# (2)这种方式会导入所有不以下划线（_）开头的名称。大多数情况下，不要用这个功能，这种方式向解释器导入了一批未知的名称，可能会覆盖已经定义的名称
# from fibo import *
# (3)模块名后使用 as 时，直接把 as 后的名称与导入模块绑定
# import fibo as fib
# from fibo import fib as fibonacci

# 以脚本方式执行模块
# python fibo.py <arguments>  # 这项操作将执行模块里的代码，和导入模块一样，但会把 __name__ 赋值为 "__main__"
# if __name__ == "__main__":  # 会把下列代码添加到模块末尾
#     import sys
#     fib(int(sys.argv[1]))
# 导入模块时，不运行这些代码
# 这种操作常用于为模块提供便捷用户接口，或用于测试（把模块当作执行测试套件的脚本运行）
# import fibo

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
# import fibo, sys
# print(dir(fibo))
# print(dir(sys))

# 没有参数时，dir() 列出当前定义的名称,该函数列出所有类型的名称：变量、模块、函数等
# a = [1, 2, 3, 4, 5]
# import fibo
# fib = fibo.fib
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

# 8 错误和异常

























