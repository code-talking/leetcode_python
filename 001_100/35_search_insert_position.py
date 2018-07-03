# -*- coding: utf-8 -*-
'''
    Author:   bl
    Date:   5/20/18
    Time:   3:21 PM
    Package 
    File    35_search_insert_position.py
    Description
    
'''
class Solution:
    def search_insert(self, nums, target):
        if nums is None:
            return -1
        if len(nums) == 0:
            return 0
        left = 0
        right = len(nums) - 1
        i = 0
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                if mid + 1 <= right:
                    left = mid + 1
                else:
                    return mid + 1
            else:
                if mid - 1 >= left:
                    right = mid - 1
                else:
                    return mid

lst = [1, 3, 5, 6]
target = 7
test = Solution()
rst = test.search_insert(lst, target)
print('rst = ', rst)