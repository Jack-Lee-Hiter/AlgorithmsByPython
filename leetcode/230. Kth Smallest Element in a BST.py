'''
Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.
'''
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def kthSmallest(self, pRoot, k):
        if k <= 0 or not pRoot:
            return None
        treeStack, nodesQue = [], []
        pNode = pRoot
        while pNode or len(treeStack):
            while pNode:
                treeStack.append(pNode)
                pNode = pNode.left
            if len(treeStack):
                pNode = treeStack.pop()
                nodesQue.append(pNode)
                pNode = pNode.right
        if k > len(nodesQue):
            return None
        return nodesQue[k-1].val