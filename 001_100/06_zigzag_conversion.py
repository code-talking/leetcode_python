# -*- coding: utf-8 -*-
'''
    Author:   bl
    Date:   5/23/18
    Time:   2:54 PM
    Package 
    File    06_zigzag_conversion.py
    Description
    
'''
class Solution:
    def convert(self, s, numRows):
        if s is None or numRows == 0:
            return None

        rst = []
        num = 2 * numRows - 2
        for pos in range(len(s)):
            if pos < numRows:
                rst.append(s[pos])
            else:
                i = pos % (num - 1)
                if i < numRows:
                    # rst[i].join(s[pos])
                    rst[i] += s[pos]
                else:
                    # rst[numRows - 1 - (i - numRows)].join(s[pos])
                    rst[numRows - 1 - (i + 1 - numRows)] += s[pos]

            print('pos = ', pos, '\t\trst :', rst)

        ss = ''.join(rst)
        return ss

test = Solution()
s = 'PAYPALISHIRING'
numRows = 4
rst1 = test.convert(s, numRows)
print('rst : ', rst1)