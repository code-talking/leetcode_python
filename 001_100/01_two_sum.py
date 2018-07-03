# -*- coding: utf-8 -*-
'''
    Author:   bl
    Date:   5/17/18
    Time:   7:25 PM
    Package 
    File    01_two_sum.py
    Description
    
'''
def p():
    print('-------------------------------------------------------------------------')

class Solution:
    def two_sum(self, nums, target):
        rst = [-1, -1]
        if (len(nums) <= 1):
            return rst
        remaining = {}
        for i in range(len(nums)):
            if nums[i] in remaining:
                return [remaining[nums[i]], i]
            else :
                remaining[target - nums[i]] = i
        return rst



test = Solution()
nums_1 = [1, 2, 3, 4, 5, 10]
target_1 = 12
rst_1 = test.two_sum(nums_1, target_1)
print(nums_1, '\t\t', target_1)
print('rst = ', rst_1)

p()

nums_2 = [1, 2, 3, 4, 5]
target_2 = 100
rst_2 = test.two_sum(nums_2, target_2)
print(nums_2, '\t\t', target_2)
print('rst = ', rst_2)

p()
nums = [1, 2, 3, 4]