# -*- coding: utf-8 -*-
'''
    Author:   bl
    Date:   6/2/18
    Time:   11:27 AM
    Package 
    File    19_remove_nth_node_from_end_of_list.py
    Description
    
'''
from module_helper import ListNode

class Solution:
    def removeNthFromEnd(self, head, n):
        if head is None:
            return head

        len_head = self.__findLen(head)
        if len_head == n:
            return head.next

        if n == 0 or n % len_head == 0:
            return head

        pos_removed = n % len_head
        dummy = ListNode(0)
        dummy.next = head

        left_len = len_head - pos_removed
        count = 1
        while count < left_len:
            head = head.next
            count += 1


        new_head = head.next.next
        if new_head is None:
            head.next = None
            return dummy.next

        head.next = new_head
        return dummy.next

    def __findLen(self, head):
        count = 0
        while head is not None:
            count += 1
            head = head.next
        return count








list_node = ListNode(1)
list_node.next = ListNode(2)
list_node.next.next = ListNode(3)
list_node.next.next.next = ListNode(4)
list_node.next.next.next.next = ListNode(5)
