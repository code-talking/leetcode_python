# -*- coding: utf-8 -*-
'''
    Author:   bl
    Date:   6/17/18
    Time:   8:05 PM
    Package 
    File    test_11.py
    Description
    
'''
from module_helper import TreeNode as tn
from module_helper import pp
root = tn.TreeNode(5)
root.left = tn.TreeNode(3)
root.right = tn.TreeNode(8)

root.left.right = tn.TreeNode(4)
node = root
node.preorder_recursion(node)
pp.p()

node = root
node.inorder_recursion(node)
pp.p()

node = root
node.postorder_recursion(node)