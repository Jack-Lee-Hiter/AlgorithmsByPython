# -*- coding:utf-8 -*-
'''
求树的宽度
即树的某层所含结点数目最多, 则打印出该数字
'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def widthOfTree(self, pRoot):
        if pRoot == None:
            return 0
        nodeQue = [pRoot]
        levelCount, level, maxNum = {0: 1}, 0, 1
        while len(nodeQue):
            tempQue = nodeQue[:levelCount[level]]
            curNodeNum = 0
            while len(tempQue) > 0:
                tempQue.pop(0)
                pNode = nodeQue.pop(0)
                if pNode.left:
                    nodeQue.append(pNode.left)
                    curNodeNum += 1
                if pNode.right:
                    nodeQue.append(pNode.right)
                    curNodeNum += 1
            level += 1
            if level not in levelCount.keys():
                levelCount[level] = curNodeNum
            if curNodeNum > maxNum:
                maxNum = curNodeNum
        return maxNum


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
pNode3.left = pNode7

S = Solution()
width = S.widthOfTree(pNode1)
print(width)