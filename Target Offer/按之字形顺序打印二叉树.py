'''
请实现一个函数按照之字形打印二叉树，
即第一行按照从左到右的顺序打印，第二层按照从右至左的顺序打印，第三行按照从左到右的顺序打印，其他行以此类推。
'''

# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def Print(self, pRoot):
        if pRoot == None:
            return []
        result = []
        nodes = [pRoot]
        right, left = True, False
        while nodes:
            currentStack = []
            nextStack = []
            if right:
                for node in nodes:
                    currentStack.append(node.val)
                    if node.left != None:
                        nextStack.append(node.left)
                    if node.right != None:
                        nextStack.append(node.right)
                nextStack.reverse()
            elif left:
                for node in nodes:
                    currentStack.append(node.val)
                    if node.right != None:
                        nextStack.append(node.right)
                    if node.left != None:
                        nextStack.append(node.left)
                nextStack.reverse()
            right, left = left, right
            result.append(currentStack)
            nodes = nextStack
        return result