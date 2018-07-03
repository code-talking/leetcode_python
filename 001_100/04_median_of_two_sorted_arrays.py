# -*- coding: utf-8 -*-
'''
    Author:   bl
    Date:   5/21/18
    Time:   4:40 PM
    Package 
    File    04_median_of_two_sorted_arrays.py
    Description
    
'''
class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        len1 = len(nums1)
        len2 = len(nums2)
        len_total = len1 + len2

        if len_total % 2 == 1:
            pos = len_total // 2
            return self.__helper(nums1, len1, nums2, len2, pos)
        pos_right = len_total // 2
        pos_left = len_total // 2 - 1
        return (self.__helper(nums1, len1, nums2, len2, pos_left) + self.__helper(nums1, len1, nums2, len2, pos_right)) / 2

    def __helper(self, nums1, len1, nums2, len2, pos):
        pos1, pos2 = 0, 0
        rst = 0
        while pos >= 0 and pos1 < len1 and pos2 < len2:
            if nums1[pos1] <= nums2[pos2]:
                rst = nums1[pos1]
                pos1 += 1
            else:
                rst = nums2[pos2]
                pos2 += 1
            pos -= 1

        while pos >= 0 and pos1 < len1:
            rst = nums1[pos1]
            pos1 += 1
            pos -= 1

        while pos >= 0 and pos2 < len2:
            rst = nums2[pos2]
            pos2 += 1
            pos -= 1
        return rst

nums1 = [1, 2, 3, 4, 5]
nums2 = [2, 9, 10]
test = Solution()
rst = test.findMedianSortedArrays(nums1, nums2)
print('rst = ', rst)