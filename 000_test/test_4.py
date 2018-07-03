# -*- coding: utf-8 -*-
'''
    Author:   bl
    Date:   5/20/18
    Time:   10:43 AM
    Package 
    File    test_4.py
    Description
    
'''


def generateParenthesis(n):
    def generate(p, left, right, parens = []):
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

rst = generateParenthesis(1)