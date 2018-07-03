# -*- coding: utf-8 -*-
'''
    Author:   bl
    Date:   5/17/18
    Time:   7:36 PM
    Package 
    File    02_add_two_numbers.py
    Description
    
'''
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def print_ListNode(self, listnode):
        while listnode is not None:
            print(listnode.val)
            listnode = listnode.next

class Solution:
    def add_two_numbers(self, l1, l2):
        dummy = curr = ListNode(0)
        carry = 0
        while l1 or l2 or carry:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
            curr.next = ListNode(carry % 10)
            curr = curr.next
            carry //= 10
        return dummy.next

test = Solution()
l1 = ListNode(1)
l1.next = ListNode(2)

l2 = ListNode(0)
l2.next = ListNode(1)
l2.next.next = ListNode(3)

rst = test.add_two_numbers(l1, l2)
while rst is not None:
    print(rst.val)
    rst = rst.next

if __name__ == '__main__':
    print('hello')