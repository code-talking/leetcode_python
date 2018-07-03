# -*- coding: utf-8 -*-
'''
    Author:   bl
    Date:   6/17/18
    Time:   8:02 PM
    Package 
    File    TreeNode.py
    Description
    
'''
class TreeNode():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    level = 0
    '''
        二叉树的三种遍历
        递归写法
    '''
    def preorder_recursion(self, root):
        if root is None:
            return
        print('level = ', self.level,'\t\troot.val = ', root.val)
        self.level += 1
        self.preorder_recursion(root.left)
        # self.level -= 1
        # self.level += 1
        self.preorder_recursion(root.right)
        self.level -= 1

    def inorder_recursion(self, root):
        if root is None:
            return
        self.level += 1
        self.inorder_recursion(root.left)
        self.level -= 1
        print('level = ', self.level, '\t\tval = ', root.val)
        self.level += 1
        self.inorder_recursion(root.right)
        self.level -= 1

    def postorder_recursion(self, root):
        if root is None:
            return
        self.level += 1
        self.postorder_recursion(root.left)
        # self.level -= 1
        # self.level += 1
        self.postorder_recursion(root.right)
        self.level -= 1
        print('level = ', self.level, '\t\tval = ', root.val)

    '''
        二叉树的三种遍历
        非递归
    '''
    def preorder_loop(self, root):
        return