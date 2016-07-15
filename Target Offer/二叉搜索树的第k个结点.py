'''
给定一颗二叉搜索树，请找出其中的第k大的结点。例如，
    5
   / \
  3  7
 /\ /\
2 4 6 8 中，
按结点数值大小顺序第三个结点的值为4。
'''

# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 返回对应节点TreeNode
    def __init__(self):
        self.treeNode = []
    def preOrder(self, pRoot):
        if len(self.treeNode) < 0:
            return None
        if pRoot.left:
            self.preOrder(pRoot.left)
        self.treeNode.append(pRoot)
        if pRoot.right:
            self.preOrder(pRoot.right)
    def KthNode(self, pRoot, k):
        if k == 0 or pRoot == None:
            return
        self.preOrder(pRoot)
        if len(self.treeNode) < k:
            return None
        return self.treeNode[k-1]