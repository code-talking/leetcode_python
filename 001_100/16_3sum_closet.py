# -*- coding: utf-8 -*-
'''
    Author:   bl
    Date:   5/30/18
    Time:   10:10 PM
    Package 
    File    16_3sum_closet.py
    Description
    
'''
class Solution:
    def three_sum_closest(self, nums, target):
        rst = None
        if nums is None or len(nums) < 3:
            return rst

        nums.sort()
        start, left, right = 0, 1, len(nums) - 1
        rst = nums[start] + nums[left] + nums[right]
        for start in range(len(nums) - 2):
            left = start + 1
            right = len(nums) - 1

            while left < right:
                three_sum = nums[start] + nums[left] + nums[right]
                if three_sum == target:
                    rst = three_sum
                    return rst

                if abs(three_sum - target) < abs(rst - target):
                    rst = three_sum

                if three_sum - target < 0:
                    left += 1
                else:
                    right -= 1
        return rst

test = Solution()
nums = [-1, 2, 1, -4]
target = 1
rst = test.three_sum_closest(nums = nums, target = target)
print('rst = ', rst)