# -*- coding: utf-8 -*-
'''
    Author:   bl
    Date:   5/25/18
    Time:   5:58 PM
    Package 
    File    15_3sum.py
    Description
    
'''
class Solution:
    def threeSum(self, nums):
        if nums is None or len(nums) < 3:
            return None

        nums.sort()
        print("nums : ", nums)
        rst = []
        start, left, right = 0, 1, len(nums) - 1
        while start < len(nums) - 2:
            if start == 0 or (start > 0 and nums[start] != nums[start - 1]):
                left, right = start + 1, len(nums) - 1
                target = - nums[start]

                while left < right:
                    if nums[left] + nums[right] == target:
                        temp = [nums[start], nums[left], nums[right]]
                        rst.append(temp)

                        while left < right:
                            if nums[left + 1] == nums[left]:
                                left += 1
                                continue
                            else:
                                # left += 1
                                break
                        while left < right:
                            if nums[right - 1] == nums[right]:
                                right -= 1
                                continue
                            else:
                                # right -= 1
                                break
                        left += 1
                        right -= 1

                        # ################################################################
                        # 比较区别
                        # while mid < right and nums[mid] == nums[mid + 1]:
                        #     mid += 1
                        # while mid < right and nums[right] == nums[right - 1]:
                        #     right -= 1
                        # mid += 1
                        # right -= 1
                        # ################################################################

                    elif nums[left] + nums[right] < target:
                        left += 1
                    else:
                        right -= 1
            start += 1
        return rst


test = Solution()
nums = [-1, 0, 1, 2, -1, -4]
# nums = [0, 0, 0, 0]
rst = test.threeSum(nums)
print('rst = ', rst)