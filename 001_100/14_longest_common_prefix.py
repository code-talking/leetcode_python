# -*- coding: utf-8 -*-
'''
    Author:   bl
    Date:   5/24/18
    Time:   9:49 PM
    Package 
    File    14_longest_common_prefix.py
    Description
    
'''
class Solution:
    def longestCommonPrefix(self, strs):
        if strs is None:
            return None

        if len(strs) == 0:
            return ''

        min_len = len(strs[0])
        for i in range(len(strs)):
            min_len = min(min_len, len(strs[i]))

        rst_len = 0
        for pos in range(min_len):
            if self.__is_same(strs, pos):
                rst_len += 1
            else:
                break
        return strs[0][ : rst_len]

    def __is_same(self, strs, pos):
        c = strs[0][pos]
        for i in range(1, len(strs)):
            if c != strs[i][pos]:
                return False

        return True

test = Solution()
strs = ['flow', 'flower', 'flight']
rst = test.longestCommonPrefix(strs)
print('rst = ', rst)