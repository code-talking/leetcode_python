# -*- coding: utf-8 -*-
'''
    Author:   bl
    Date:   5/21/18
    Time:   3:03 PM
    Package 
    File    03_longest_substring_without_duplicates.py
    Description
    
'''
class Solution:
    def lengthOfLongestSubstring(self, s):
        if s is None:
            return -1

        if len(s) == 0:
            return 0

        visited = {}
        slow, fast = 0, 0
        max_len = 0
        for fast in range(len(s)):
            if s[fast] in visited:
                '''
                    slow与slow还不同，每一次需要移动slow的位置，但是，移动到哪里，还需要进行判断
                    判断的原则就是：
                        移动过后，必须把所有的重复的字符全部排除在外，所以选取最大
                '''
                slow = max(visited[s[fast]] + 1, slow)
            # 出现重复之前就是没出现重复，那么下面两行代码就没问题
            max_len = max(max_len, fast - slow + 1)
            visited[s[fast]] = fast
            print('fast = ', fast, '\t\tslow = ', slow, '\t\tmax_len = ', max_len, '\t\tvisited: ', visited)
        return max_len

s = 'abba'
test = Solution()
rst = test.lengthOfLongestSubstring(s)
print('rst = ', rst)
