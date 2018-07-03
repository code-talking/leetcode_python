# -*- coding: utf-8 -*-
'''
    Author:   bl
    Date:   5/24/18
    Time:   6:04 PM
    Package 
    File    12_integer_to_roman.py
    Description
    
'''
class Solution:
    def intToRoman(self, num):
        tag = 0
        rst = ''
        global signal
        signal = [
            ['I', 'V', 'X'],
            ['X', 'L', 'C'],
            ['C', 'D', 'M']
        ]

        while num >= 0 and tag <= 2:
            remaining = num % 10
            if remaining < 4:
                rst = signal[tag][0] * remaining + rst
            elif remaining == 4:
                rst = signal[tag][0] + signal[tag][1] + rst
            elif remaining < 9:
                rst = signal[tag][1] + signal[tag][0] * (remaining - 5) + rst
            else:
                rst = signal[tag][0] + signal[tag][2] + rst
            tag += 1
            num //= 10

        if num > 0:
            rst = 'M' * num + rst

        return rst

test = Solution()
num = 3999
rst = test.intToRoman(num)
print('rst = ', rst)