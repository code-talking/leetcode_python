# -*- coding: utf-8 -*-
'''
    Author:   bl
    Date:   5/23/18
    Time:   4:18 PM
    Package 
    File    07_reverse_integer.py
    Description
    
'''
import math as m
class Solution():
    def reverse(self, x):
        max_num = m.pow(2, 31) - 1
        min_num = m.pow(-2, 31)

        if x >= 0:
            rst = self.__calculate(x)
        else:
            rst = - self.__calculate(x * -1)
        return rst if rst <= max_num and rst >= min_num else 0

    def __calculate(self, num):
        rst = 0
        while num // 10 > 0:
            remaining = num % 10
            rst = 10 * rst + remaining
            num //= 10
        rst = rst * 10 + num
        return rst

test = Solution()
num = -1230
rst = test.reverse(num)
print('rst = ', rst)