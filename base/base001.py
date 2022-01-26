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

# def my_function():  # 文档字符串
#     """Do nothing, but document it.
#
#     No, really, it doesn't do anything.
#     """
#     pass
# print(my_function.__doc__)

# def f(ham: str, eggs: str = 'eggs') -> str:
#     print("Annotations:", f.__annotations__)  # 函数注解
#     print("Arguments:", ham, eggs)
#     return ham + ' and ' + eggs
# f('spam')

# 3 数据结构
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

# stack = [3, 4, 5]  # 用列表实现堆栈
# stack.append(6)
# stack.append(7)
# print(stack)  # [3, 4, 5, 6, 7]
# print(stack.pop())  # 7
# print(stack)  # [3, 4, 5, 6]

from collections import deque






