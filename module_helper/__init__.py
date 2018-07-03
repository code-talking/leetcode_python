# -*- coding: utf-8 -*-
'''
    Author:   bl
    Date:   5/27/18
    Time:   11:25 PM
    Package 
    File    __init__.py.py
    Description
    
'''
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def p_node(self):
        i = 0
        while self is not None:
            print('i = ', i, '\t\tval = ', self.val)
        print('----------------------------------------------')