'''
输入一颗二叉树和一个整数，打印出二叉树中结点值的和为输入整数的所有路径。
路径定义为从树的根结点开始往下一直到叶结点所经过的结点形成一条路径。
'''
# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
        if root == None:
            return []
        if root.val > expectNumber:
            return []
        elif root.val == expectNumber:
            if root.left or root.right:
                return []                   # 因为路径的定义是从根节点到叶节点所经过的结点, 如果是根结点到任意可到达结点的和为待求值, 可以去掉这个判定
            else:
                return [[expectNumber]]

        stack = []
        if root.left:
            stackLeft = self.FindPath(root.left, expectNumber-root.val)
            if stackLeft:
                for i in stackLeft:
                    i.insert(0, root.val)
                    stack.append(i)
        if root.right:
            stackRight = self.FindPath(root.right, expectNumber-root.val)
            if stackRight:
                for i in stackRight:
                    i.insert(0, root.val)
                    stack.append(i)

        if stack:
            return stack
        else:
            return []

pNode1 = TreeNode(10)
pNode2 = TreeNode(5)
pNode3 = TreeNode(12)
pNode4 = TreeNode(4)
pNode5 = TreeNode(7)


pNode1.left = pNode2
pNode1.right = pNode3
pNode2.left = pNode4
pNode2.right = pNode5


S = Solution()
print(S.FindPath(pNode1, 22))