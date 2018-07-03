# -*- coding: utf-8 -*-
'''
    Author:   bl
    Date:   5/23/18
    Time:   5:22 PM
    Package 
    File    08_string_to_integer.py
    Description
    
'''
class Solution:
    def myAtoi(self, str):
        s = str.strip()

        if s == '':
            return 0

        if len(s) == 1 and not s[0].isdigit():
            return 0

        if not s[0].isdigit() and s[0] != '-' and s[0] != '+':
            return 0

        rst = 0
        max_num = 2 ** 31 - 1
        min_num = (-2) ** 31

        if s[0] == '-' or s[0] == '+':
            if not s[1].isdigit():
                return 0
            elif s[0] == '+':
                rst = self.find_num(s[1:])
            else:
                rst = - self.find_num(s[1:])
        else:
            rst = self.find_num(s)

    def find_num(self, s):
        rst = 0
        for i in range(len(s)):
            if s[i].isdigit():
                rst = rst * 10 + int(s[i])
            else:
                break
        return rst