# -*- coding: utf-8 -*-
'''
    Author:   bl
    Date:   5/20/18
    Time:   1:31 AM
    Package 
    File    81_search_in_rotated_sorted_array_2.py
    Description
    
'''
def p():
    print('------------------------------------------------------------------------------')

class Solution:
    def search_right(self, nums, target):
        ''''''
        '''
        :type nums: List[int]
        :type target: int
        :rtype: bool
        '''

        if nums is None or len(nums) == 0:
            return False

        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return True

            if nums[mid] < nums[right]:
                if target > nums[mid] and target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
            elif nums[mid] > nums[right]:
                if target >= nums[left] and target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                right -= 1
        return False

    def seft_left(self, nums, target):
        if nums is None or len(nums) == 0:
            return False

        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return True

            if nums[mid] > nums[left]:
                if target >= nums[left] and target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            elif nums[mid] < nums[left]:
                if target > nums[mid] and target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                left += 1
        return False


lst = [1, 3, 1, 1, 1]
target = 3
test = Solution()
rst_right = test.search_right(lst, target)
print('rst_right = ', rst_right)

p()

rst_left = test.seft_left(lst, target)
print('rst_left = ', rst_left)