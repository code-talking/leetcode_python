# -*- coding: utf-8 -*-
'''
    Author:   bl
    Date:   5/17/18
    Time:   7:25 PM
    Package 
    File    1_two_sum.py
    Description
    
'''
def p():
    print('---------------------------------------------')

class Solution:
    def two_sum(self, nums, target):
        if (len(nums) <= 1):
            rst = [-1, -1]
            print('None : ', None)
            return None
        remaining = {}
        for i in range(len(nums)):
            if nums[i] in remaining:
                return [remaining[nums[i]], i]
            else :
                remaining[target - nums[i]] = i

test = Solution()
nums = [1, 2, 3, 4, 5, 10]
target = 12
rst = test.two_sum(nums, target)
print('rst = ', rst)

p()

nums = [1, 2, 3, 4, 5]
target = 100
rst = test.two_sum(nums, target)
print('rst = ', rst)

p()

print(test.two_sum([-1, 1, 2], 0))