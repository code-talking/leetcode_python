# -*- coding: utf-8 -*-
'''
    Author:   bl
    Date:   5/24/18
    Time:   9:39 PM
    Package 
    File    13_roman_to_integer.py
    Description
    
'''
'''
    罗马数字变成integer的规则：
        从右往左看，s[i]跟s[i + 1]进行比较
            s[i] < s[i + 1]
                rst = rst - s[i]代表的数字
            s[i] >= s[i + 1]
                结果相加
'''
class Solution:
    def romanToInt(self, s):
        if s is None:
            return None

        char_to_int = {'M' : 1000, 'D' : 500, 'C' : 100, 'L' : 50, 'X' : 10, 'V' : 5, 'I' : 1}
        rst = char_to_int[s[len(s) - 1]]
        for i in range(len(s) - 1):
            index = len(s) - 1 - 1 - i
            num = char_to_int[s[index]]
            if num < char_to_int[s[index + 1]]:
                rst -= num
            else:
                rst += num
        return rst

test = Solution()
s = 'MCMXCIV'
rst = test.romanToInt(s)
print('rst = ', rst)