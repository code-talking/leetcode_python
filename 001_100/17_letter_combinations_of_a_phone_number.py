# -*- coding: utf-8 -*-
'''
    Author:   bl
    Date:   5/30/18
    Time:   11:03 PM
    Package 
    File    17_letter_combinations_of_a_phone_number.py
    Description
    
'''


class Solution():
    def letter_combinations(self, digits):
        rst = []

        '''
            输入判断
        '''
        if digits is None or len(digits) == 0:
            return rst

        rst = self.__helper(digits)
        return rst

    def __helper(self, digits):
        num_dict = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        '''
                    递归的出口
        '''
        if len(digits) == 1:
            rst = list(num_dict[digits])
            return rst

        prev = self.letter_combinations(digits[: -1])
        additional = num_dict[digits[-1]]

        rst = [s + c for s in prev for c in additional]
        return rst


test = Solution()
digits = '23'
rst = test.letter_combinations(digits)
print('rst = ', rst)
