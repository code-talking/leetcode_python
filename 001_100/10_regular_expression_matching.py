# -*- coding: utf-8 -*-
'''
    Author:   bl
    Date:   5/24/18
    Time:   12:07 PM
    Package 
    File    10_regular_expression_matching.py
    Description
    
'''
class Solution:
    def isMatch(self, s, p):
        if s is None or p is None:
            return False
        row = len(s) + 1
        col = len(p) + 1
        rst = [[False for j in range(col)] for i in range(row)]

        for j in range(col):
            rst[0][j] = True

        for i in range(row):
            rst[i][0] = True

        print(rst)
test = Solution()
s = 'abc'
p = '.*'
rst = test.isMatch(s, p)
print('rst = ', rst)

