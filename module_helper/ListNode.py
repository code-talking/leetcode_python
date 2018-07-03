# -*- coding: utf-8 -*-
'''
    Author:   bl
    Date:   5/27/18
    Time:   11:25 PM
    Package 
    File    ListNode.py
    Description
    
'''
import random


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def p_node(self, lst_node):
        i = 0
        while lst_node is not None:
            print('i = ', i, '\t\tval = ', lst_node.val)
            lst_node = lst_node.next
            i += 1
        print('----------------------------------------------')
        
def p_ListNode(list_node):
    pos = 0
    while list_node is not None:
        print('pos = ', pos, '\t\tval = ', list_node.val)
        list_node = list_node.next