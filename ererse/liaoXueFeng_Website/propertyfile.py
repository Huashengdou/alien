#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 要理解property的作用，首先要明白装饰器decorator的作用。
# 本质上装饰器就是一个返回函数的高阶函数

# 定义一个装饰器函数，该函数以一个函数为参数，返回一个函数
# 装饰器的作用就是能动态增加功能，但不改变原来函数功能
def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper

# 将“@log”放在函数定义处，相当于执行：now = log(now)
# 即函数now执行了，但是增加了log中的打印功能
@log
def now():
    print('i am now!')


# property装饰器的作用就是使用属性这样简单的方式来访问类的变量
# 当对有property装饰的实例属性进行操作时，该属性是不直接暴露的，
# 而是通过getter和setter方法来实现的
# 当需要定义只读属性的时候，只定义getter方法即可。不定义setter方法就是
# 一个只读属性
class Student(object):

    @property
    def score(self):
        return self._score
    # score就是一个可读可写的属性
    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer')
        if value < 0 or value > 100:
            raise ValueError('score must be 0 ~ 100')
        self._score = value

    @property
    def age(self):
        print('i am age!')

    @age.setter
    def age(self, age):
        self._age = age

# 定义一个求面积类，其中width和height是可读可写属性，resolution是只读属性
class Screen(object):
    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, width):
        self._width = width

    @property
    def height(self):
        return self.height

    @height.setter
    def height(self, height):
        self._height = height

    @property
    def resolution(self):
        self._resolution = self._width * self._height
        return self._resolution


if __name__ == '__main__':
    s = Student()
    s.score = 60
    print(s.score)

    a = Screen()
    a.width = 1024
    a.height = 768
    print('resolution =', a.resolution)
    if a.resolution == 786432:
        print('测试通过')
    else:
        print('测试失败')
#   now()

