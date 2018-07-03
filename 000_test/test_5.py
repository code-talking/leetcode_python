# -*- coding: utf-8 -*-
'''
    Author:   bl
    Date:   5/20/18
    Time:   10:43 AM
    Package 
    File    test_5.py
    Description
    
'''
from functools import reduce

lst = [1, 2, 3, 4, 5]
rst = reduce(lambda x, y : x * y, lst)
print('rst = ', rst)