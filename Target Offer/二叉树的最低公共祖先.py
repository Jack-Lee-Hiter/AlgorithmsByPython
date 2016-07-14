'''
查找二叉搜索树两个结点的最低公共祖先
'''

# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def findParent(self, pNode1, pNode2, root):
        if pNode1 == None or pNode2 == None:
            return
        if pNode1 == pNode2:
            return
        val1 = pNode1.val
        val2 = pNode2.val
        while root != None:
            if (val1 - root.val) * (val2 - root.val) <= 0:
                return root.val
            elif val1 > root.val and val2 > root.val:
                root = root.right
            else:
                root = root.left

        return False

pNode1 = TreeNode(8)
pNode2 = TreeNode(6)
pNode3 = TreeNode(10)
pNode4 = TreeNode(5)
pNode5 = TreeNode(7)
pNode6 = TreeNode(9)
pNode7 = TreeNode(11)

pNode1.left = pNode2
pNode1.right = pNode3
pNode2.left = pNode4
pNode2.right = pNode5
pNode3.left = pNode6
pNode3.right = pNode7

S = Solution()
print(S.findParent(pNode3, pNode7, pNode1))