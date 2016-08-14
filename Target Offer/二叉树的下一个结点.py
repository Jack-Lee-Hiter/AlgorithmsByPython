'''
给定一个二叉树和其中的一个结点，请找出中序遍历顺序的下一个结点并且返回。
注意，树中的结点不仅包含左右子结点，同时包含指向父结点的指针。
'''
# -*- coding:utf-8 -*-
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None
class Solution:
    def GetNext(self, pNode):
        if pNode == None:
            return
        pNext = None
        if pNode.right != None:
            pRight = pNode.right
            while pRight.left != None:
                pRight = pRight.left
            pNext= pRight
        elif pNode.next != None:
            pCurrent = pNode
            pParent = pCurrent.next
            while pParent != None and pCurrent == pParent.right:
                pCurrent = pParent
                pParent = pCurrent.next
            pNext = pParent
        return pNext

class Solution2:
    def GetNext(self, pNode):
        # 输入是一个空节点
        if pNode == None:
            return None
        # 注意当前节点是根节点的情况。所以在最开始设定pNext = None, 如果下列情况都不满足, 说明当前结点为根节点, 直接输出None
        pNext = None
        # 如果输入节点有右子树，则下一个结点是当前节点右子树中最左节点
        if pNode.right:
            pNode = pNode.right
            while pNode.left:
                pNode = pNode.left
            pNext = pNode
        else:
            # 如果当前节点有父节点且当前节点是父节点的左子节点, 下一个结点即为父节点
            if pNode.next and pNode.next.left == pNode:
                pNext = pNode.next
            # 如果当前节点有父节点且当前节点是父节点的右子节点, 那么向上遍历
            # 当遍历到当前节点为父节点的左子节点时, 输入节点的下一个结点为当前节点的父节点
            elif pNode.next and pNode.next.right == pNode:
                pNode = pNode.next
                while pNode.next and pNode.next.right == pNode:
                    pNode = pNode.next
                # 遍历终止时当前节点有父节点, 说明当前节点是父节点的左子节点, 输入节点的下一个结点为当前节点的父节点
                # 反之终止时当前节点没有父节点, 说明当前节点在位于根节点的右子树, 没有下一个结点
                if pNode.next:
                    pNext = pNode.next
        return pNext