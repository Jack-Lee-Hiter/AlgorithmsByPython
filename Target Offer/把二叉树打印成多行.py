'''
从上到下按层打印二叉树，同一层结点从左至右输出。每一层输出一行。
'''

# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 返回二维列表[[1,2],[4,5]]
    def Print(self, pRoot):
        if pRoot == None:
            return []
        nodes = []
        tempNodes = []
        result = []
        nodes.append(pRoot)
        while nodes:
            levelResult = []
            for node in nodes:
                levelResult.append(node.val)
                if node.left != None:
                    tempNodes.append(node.left)
                if node.right != None:
                    tempNodes.append(node.right)
            result.append(levelResult)
            nodes = tempNodes
            tempNodes = []
        return result