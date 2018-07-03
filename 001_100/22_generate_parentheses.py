# -*- coding: utf-8 -*-
'''
    Author:   bl
    Date:   6/2/18
    Time:   12:26 PM
    Package 
    File    22_generate_parentheses.py
    Description
    
'''
class Solution:
    def generateParenthesis(self, n):
    #     return self.__helper(n, 0)
    #
    # def __helper(self, n, open = 0):
    #     if n == 0:
    #         return [')' * open]
    #     if open == 0:
    #         return ['(' + x for x in self.__helper(n - 1, 1)]
    #     else:
    #         return [')' +  x for x in self.__helper(n, open - 1)] + ['(' + x for x in self.__helper(n - 1, open + 1)]

        """
        :type n: int
        :rtype: List[str]
        """
        def generate(p, left, right, parens=[]):
            if left:
                generate(p + '(', left - 1, right)
                print('left = ', left, '\t\tright = ', right, '\t\tp = ', p)
            if right > left:
                generate(p + ')', left, right - 1)
                print('\t\t\tleft = ', left, '\t\tright = ', right, '\t\tp = ', p)
            if not right:
                parens += p,
                print('-----------------------')
                print('left = ', left, '\t\tright = ', right, '\t\tp = ', p)
                print('-----------------------')
            return parens

        return generate('', n, n)

test = Solution()
n = 2
rst = test.generateParenthesis(n)
print('rst = ', rst)