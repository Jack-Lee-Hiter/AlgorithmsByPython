'''
反转链表
输入一个链表，反转链表后，输出链表的所有元素
'''

# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        pReversedHead = None
        pNode = pHead
        pPrev = None
        while pNode != None:
            pNext = pNode.next

            if pNext == None:
                pReversedHead = pNode

            pNode.next = pPrev
            pPrev = pNode
            pNode = pNext
        return pReversedHead
    # 递归实现反转链表
    def ReverseListRec(self, pHead):
        if not pHead or not pHead.next:
            return pHead
        else:
            pReversedHead = self.ReverseList(pHead.next)
            pHead.next.next = pHead
            pHead.next = None
            return pReversedHead

node1 = ListNode(10)
node2 = ListNode(11)
node3 = ListNode(13)
node1.next = node2
node2.next = node3

S = Solution()
p = S.ReverseList(node1)
print(p.next.val)