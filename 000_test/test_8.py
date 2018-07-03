# -*- coding: utf-8 -*-
'''
    Author:   bl
    Date:   6/2/18
    Time:   8:24 PM
    Package 
    File    test_8.py
    Description
    
'''
from module_helper import pp
# rst = []
# def test_square():
#     global rst
#     rst.append('[]')
#     # return rst
#
# def test_curly():
#     global rst
#     rst.append('{}')
#
# test_square()
# print('rst = ', rst)
#
# test_curly()
# print('rst = ', rst)


class test():
    test_rst = []
    var = 0
    def test_square(self):
        test.test_rst.append('[]')
        print('inside test_square method')
        print(test.test_rst)

    def test_curly(self):
        test.test_rst.append('{}')
        print('inside test_curly method')
        print(test.test_rst)



t = test()
# print(t.test_rst)
# pp.p()
#
# t.test_square()
# print(t.test_square())
# pp.p()
#
# t.test_curly()
# print(t.test_curly())
# pp.p()
t.test_square()
pp.p()

t.test_curly()
pp.p()