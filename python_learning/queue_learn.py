# -*- coding: utf-8 -*-
'''
    Author:   bl
    Date:   6/24/18
    Time:   7:23 PM
    Package 
    File    queue_learn.py
    Description
    
'''
from queue import Queue
from module_helper import pp
q = Queue()
print('size = ', q.qsize())
pp.p()

s = 'Hello'
for ss in enumerate(s):
    q.put(ss[1])

while not q.empty():
    print('size = ', q.qsize(), '\t\thead = ', q.get())

pp.p()