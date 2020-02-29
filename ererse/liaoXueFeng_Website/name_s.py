#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"a test module"

__author__ = 'yan'

import sys


def test():
    args = sys.argv
    if len(args) == 1:
        print("hello world!")
    elif len(args) == 2:
        print("hello, %s!" % args[1])
    else:
        print(args)
        print("too many arguments")


# 在命令行运行该模块时，python解释器把一个特殊变量__name__置为__main__，而如果在
# 其他地方导入该模块时，该if判断会失败。
if __name__ == '__main__':
    test()


