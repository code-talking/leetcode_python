# -*- coding: utf-8 -*-
'''
    Author:   bl
    Date:   5/19/18
    Time:   9:38 PM
    Package 
    File    162_find_peak_element.py
    Description
    
'''
class Solution:
    def find_peak_ele(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums is None or len(nums) == 0:
            return 0
        left = 0
        right = len(nums) - 1
        while left < right:
            mid_1 = (left + right) // 2
            mid_2 = mid_1 + 1
            if nums[mid_1] < nums[mid_2]:
                left = mid_2
            else:
                right = mid_1
        return left

lst = [1, 2, 1, 3, 4, 5, 2, 4, 3]
test = Solution()
rst = test.find_peak_ele(lst)
print('rst = ', rst, '\t\tnums = ', lst[rst])