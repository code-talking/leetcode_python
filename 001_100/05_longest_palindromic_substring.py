# -*- coding: utf-8 -*-
'''
    Author:   bl
    Date:   5/21/18
    Time:   9:03 PM
    Package 
    File    05_longest_palindromic_substring.py
    Description
    
'''
def p():
    print('--------------------------------------------------------------')

class Solution:
    def longestPalindrome(self, s):
        if s is None or len(s) == 0:
            return 0

        ss = ''
        len_ss = 2 * len(s) - 1
        for i in range(len_ss):
            if i % 2 == 0:
                ss += s[i // 2]
            else:
                ss += '*'

        return self.odd_str(ss)

    def odd_str(self, s):
        gaps = len(s) // 2
        rst = ''
        rsts = set()
        for pos in range(len(s)):
            gap = 0
            left = pos - gap
            right = pos + gap
            while gap <= gaps and left >= 0 and right < len(s):
                if s[left] != s[right]:
                    break
                else:
                    if right - left + 1 >= len(rst):
                        rst = s[left: right + 1]
                        rsts.add(rst)
                    gap += 1
                    left = pos - gap
                    right = pos + gap
        max_len = 0
        for k in rsts:
            temp = k.replace('*', '')
            new_len = len(temp)
            if new_len >= max_len:
                rst = temp
                max_len = new_len
        return rst

test = Solution()
s = 'ccd'
rst = test.longestPalindrome(s)
print('rst = ', rst)
p()
