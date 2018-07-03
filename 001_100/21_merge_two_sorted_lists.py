# -*- coding: utf-8 -*-
'''
    Author:   bl
    Date:   5/27/18
    Time:   5:58 PM
    Package 
    File    21_merge_two_sorted_lists.py
    Description
    
'''
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        '''
        :param l1: ListNode
        :param l2: ListNode
        :return:
        '''
        if l1 is None:
            return l2
        if l2 is None:
            return l1

        dummy = head = ListNode(0)
        while l1 and l2:
            if l1.val <= l2.val:
                head.next = ListNode(l1.val)
                l1 = l1.next
                head = head.next
            else:
                head.next = ListNode(l2.val)
                l2 = l2.next
                head = head.next

        if l1:
            head.next = l1
        if l2:
            head.next = l2

        return dummy.next

l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(4)

l2 = ListNode(1)
l2.next = ListNode(3)
l2.next.next = ListNode(4)

test = Solution()
rst = test.mergeTwoLists(l1, l2)
count = 0
while rst:
    print('pos = ', count, '\t\trst.val = ', rst.val)
    rst = rst.next
    count += 1