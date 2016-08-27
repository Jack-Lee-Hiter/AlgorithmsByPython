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
    # 存储点的时候按照奇数层和偶数层分别存储
    def Print(self, pRoot):
        if not pRoot:
            return []
        result, nodes = [], [pRoot]
        right = True
        while nodes:
            curStack, nextStack = [], []
            if right:
                for node in nodes:
                    curStack.append(node.val)
                    if node.left:
                        nextStack.append(node.left)
                    if node.right:
                        nextStack.append(node.right)
            else:
                for node in nodes:
                    curStack.append(node.val)
                    if node.right:
                        nextStack.append(node.right)
                    if node.left:
                        nextStack.append(node.left)
            nextStack.reverse()
            right = not right
            result.append(curStack)
            nodes = nextStack
        return result
    # 转换思路，存储的时候一直从左向右存储，打印的时候根据不同的层一次打印
    def zigzagLevelOrder(self, root):
        if not root:
            return []
        levels, result, leftToRight = [root], [], True
        while levels:
            curValues, nextLevel = [], []
            for node in levels:
                curValues.append(node.val)
                if node.left:
                    nextLevel.append(node.left)
                if node.right:
                    nextLevel.append(node.right)
            if not leftToRight:
                curValues.reverse()
            if curValues:
                result.append(curValues)
            levels = nextLevel
            leftToRight = not leftToRight
        return result


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
aList = S.Print(pNode1)
print(aList)