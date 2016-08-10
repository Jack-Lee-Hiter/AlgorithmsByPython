'''
输入一棵二叉树，判断该二叉树是否是平衡二叉树。
'''

# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def __init__(self):
        self.flag = True

    def IsBalanced_Solution(self, pRoot):
        self.getDepth(pRoot)
        return self.flag

    def getDepth(self, pRoot):
        if pRoot == None:
            return 0
        left = 1 + self.getDepth(pRoot.left)
        right = 1 + self.getDepth(pRoot.right)

        if abs(left - right) > 1:
            self.flag = False

        return left if left > right else right
class Solution2:
    def getDepth(self, pRoot):
        if pRoot == None:
            return 0
        return max(self.getDepth(pRoot.left), self.getDepth(pRoot.right)) + 1
    def IsBalanced_Solution(self, pRoot):
        if pRoot == None:
            return True
        if abs(self.getDepth(pRoot.left)-self.getDepth(pRoot.right)) > 1:
            return False
        return self.IsBalanced_Solution(pRoot.left) and self.IsBalanced_Solution(pRoot.right)


pNode1 = TreeNode(1)
pNode2 = TreeNode(2)
pNode3 = TreeNode(3)
pNode4 = TreeNode(4)
pNode5 = TreeNode(5)
pNode6 = TreeNode(6)
pNode7 = TreeNode(7)

pNode1.left = pNode2
pNode1.right = pNode3
pNode2.left = pNode4
pNode2.right = pNode5
pNode3.right = pNode6
pNode5.left = pNode7

S = Solution2()
print(S.getDepth(pNode1))