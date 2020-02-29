#!/usr/bin/env python3
# -*- coding:utf-8 -*-


class Student(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def printfinfo(self):
        print("%s: %s" % (self.name, self.age))


if __name__ == '__main__':
    student = Student('Mary', 10)
    student.printfinfo()


