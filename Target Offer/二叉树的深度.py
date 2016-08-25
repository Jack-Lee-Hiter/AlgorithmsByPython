'''
输入一棵二叉树，求该树的深度。
从根结点到叶结点依次经过的结点（含根、叶结点）形成树的一条路径，最长路径的长度为树的深度。
'''

# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 递归解法, 简单直接, 时间复杂度O(n), 空间复杂度O(logn)
    def TreeDepth(self, pRoot):
        if pRoot == None:
            return 0
        else:
            return max(self.TreeDepth(pRoot.left), self.TreeDepth(pRoot.right)) + 1
    # 非递归算法，利用一个栈以及一个标志位栈
    def TreeDepth2(self, pRoot):
        if not pRoot:
            return 0
        depth = 0
        stack, tag = [], []
        pNode = pRoot
        while pNode or stack:
            while pNode:
                stack.append(pNode)
                tag.append(0)
                pNode = pNode.left
            if tag[-1] == 1:
                depth = max(depth, len(stack))
                stack.pop()
                tag.pop()
                pNode = None
            else:
                pNode = stack[-1]
                pNode = pNode.right
                tag.pop()
                tag.append(1)
        return depth