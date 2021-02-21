#  -*- coding: utf-8 -*-
#  Copyright (c) 2021. syshlangcom
#  File: 注释.py
#  Description:
#  Author: sunys
#  Date: 2021/2/21 上午10:50
#  since:

#  1、块注释
#  “#”号后空一格，段落件用空行分开（同样需要“#”号）

# 块注释
# 块注释
# 这是一个main方法用于说明块注释
if __name__ == '__main__':
    print('块注释 “#”号后空一格，段落件用空行分开（同样需要“#”号）')

# 2、行注释
# 为了提高可读性,至少使用两个空格和语句分开

if __name__ == '__main__':  # 这是一个main方法
    print('行注释 为了提高可读性,至少使用两个空格和语句分开')

# 3、文档注释
# 文档注释以 """ 开头和结尾, 首行不换行, 如有多行, 末行必需换行
"""
作为文档的Docstring一般出现在模块头部、函数和类的头部，这样在python中可以通过对象的__doc__对象获取文档. 
编辑器和IDE也可以根据Docstring给出自动提示.
"""


def functionSum():
    """
    计算并返回输入的1到1000范围内的a到b两数的和
    :return:
    """


a, b = map(int, input().split())
if 1 <= a <= 1000 and 1 <= b <= 1000:
    print(a + b)
else:
    print("输入错误")

if __name__ == '__main__':
    print(f'文档注释以 """ 开头和结尾, 首行不换行, 如有多行, 末行必需换行')
    functionSum()
