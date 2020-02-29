#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 上面第一行注释是为了告诉Linux系统，这是一个Python程序，Windows系统会忽略这个注释；
# 上面第二行注释是为了告诉Python解释器，按照UTF-8编码读取源代码，否则，可能会有乱码


# python内部使用r''表示单引号内的字符串默认不用转义
print('\\\t\\')
print(r'\\\t\\')

# 若输出多行，还可以使用"""内容"""
print("""line1
line2
line3
""")

print(chr(25991))

r = (85 - 72) / 72 * 100
print("提升了%.1f%%" % r)

L = ['bart', 'lisa', 'adam']
for i in L:
    print('hello, %s' % i)
