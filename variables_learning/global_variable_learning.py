# -*- coding: utf-8 -*-
'''
    Author:   bl
    Date:   6/2/18
    Time:   9:30 PM
    Package 
    File    global_variable_learning.py
    Description
    
'''
from module_helper import pp
rst = []

def add_square():
    global rst
    rst.append('[]')

def add_curly():
    global rst
    rst.append('{}')

def add_round():
    global rst
    rst.append('()')

def p():
    global rst
    print('rst =', rst)
    pp.p()

add_curly()
p()

add_round()
p()

add_square()
p()