# -*- coding: utf-8 -*-
'''
    Author:   bl
    Date:   6/2/18
    Time:   9:33 PM
    Package 
    File    class_variable_learning.py
    Description
    
'''
from module_helper import pp

class Learn():
    rst = []

    def add_square(self):
        Learn.rst.append('[]')

    def add_round(self):
        Learn.rst.append('()')

    def add_curly(self):
        Learn.rst.append('{}')


test1 = Learn()
print('test1.rst = ', test1.rst)

test1.add_square()
print('test1.rst = ', test1.rst)
pp.p()
pp.p()

test2 = Learn()
print('test2.rst = ', test2.rst)

test2.add_round()
print('test2.rst = ',test2.rst)
pp.p()
pp.p()

test3 = Learn()
print('test3.rst = ', test3.rst)

test3.add_curly()
print('test3.rst = ', test3.rst)
pp.p()
pp.p()