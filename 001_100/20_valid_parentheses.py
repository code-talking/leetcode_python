# -*- coding: utf-8 -*-
'''
    Author:   bl
    Date:   5/27/18
    Time:   4:12 PM
    Package 
    File    20_valid_parentheses.py
    Description
    
'''
class Solution:
    def isValid(self, s):
        if s is None:
            return False
        if len(s) % 2 == 1:
            return False
        stack = []
        d = {'(' : ')', '[' : ']', '{' : '}'}
        for i in range(len(s)):
            if stack == []:
                stack.append(s[i])
            else:
                c = stack[len(stack) - 1]
                if c not in d:
                    return False

                if d[c] == s[i]:
                    stack.pop()
                else:
                    stack.append(s[i])
        return stack == []

test = Solution()
s = '()'
rst = test.isValid(s)
print('rst = ', rst)