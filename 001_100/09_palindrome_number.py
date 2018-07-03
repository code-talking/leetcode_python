# -*- coding: utf-8 -*-
'''
    Author:   bl
    Date:   5/24/18
    Time:   11:20 AM
    Package 
    File    09_palindrome_number.py
    Description
    
'''
class Solution:
    def isPalindrome(self, x):
        if x < 0:
            return False
        y = x
        rev = 0
        while y // 10 > 0 and y >= rev:
            temp = y % 10
            rev = rev * 10 + temp
            if rev == y:
                return True
            y //= 10
            if rev == y:
                return True
        rev = rev * 10 + y
        # return True if rev == x else False
        return False

test = Solution()
x = 121
rst = test.isPalindrome(x)
print('rst = ', rst)