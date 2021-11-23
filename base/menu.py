#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import requests
from bs4 import BeautifulSoup
from pyepoet import *
from poems import Poetry

# genpoem()
# print("*" * 50)
# genpoem(rhyme="a")
# print("*" * 50)
# print(gpoem_string())

poetry = Poetry()

# 根据作者名，method=0 精准匹配
# poetry.for_author('李白', method=0)

# 根据作者名，method=1 相似匹配
# poetry.for_author('李', method=1)

# 根据题目
# poetry.for_name('静夜思')

# 根据类型，只有精准匹配
# poetry.for_type('词')

# 根据朝代
# poetry.for_dynasty('唐代')

# 根据内容，只有相似匹配
# poetry.for_content('静')

# 自定义
res = poetry.for_customize(method=0, author='李白', type='诗')
for item in res:
    print(item['content'])
