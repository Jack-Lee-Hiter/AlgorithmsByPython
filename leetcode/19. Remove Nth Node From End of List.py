'''
Given a linked list, remove the nth node from the end of list and return its head.
For example,
   Given linked list: 1->2->3->4->5, and n = 2.
   After removing the second node from the end, the linked list becomes 1->2->3->5.
'''
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        if not head and n <= 0:
            return None
        pNode = ListNode(0)
        pNode.next = head
        first, second = pNode, pNode
        for i in range(n):
            if first.next:
                first = first.next
            else:
                return None
        while first.next:
            first = first.next
            second = second.next
        second.next = second.next.next
        return pNode.next