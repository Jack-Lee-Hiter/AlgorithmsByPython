'''
一个链表中包含环，请找出该链表的环的入口结点。
'''

# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def MeetingNode(self, pHead):
        if pHead == None:
            return None

        pSlow = pHead.next
        if pSlow == None:
            return None
        pFast = pSlow.next
        while pFast:
            if pSlow == pFast:
                return pSlow
            pSlow = pSlow.next
            pFast = pFast.next
            if pFast:
                pFast = pFast.next

    def EntryNodeOfLoop(self, pHead):
        meetingNode = self.MeetingNode(pHead)
        if not meetingNode:
            return None

        NodeLoop = 1
        flagNode = meetingNode
        while flagNode.next != meetingNode:
            NodeLoop += 1
            flagNode = flagNode.next

        pFast = pHead
        for i in range(NodeLoop):
            pFast = pFast.next
        pSlow = pHead
        while pFast != pSlow:
            pFast = pFast.next
            pSlow = pSlow.next
        return pFast

node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)
node6 = ListNode(6)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
node6.next = node3

s = Solution()
print(s.EntryNodeOfLoop(node1).val)