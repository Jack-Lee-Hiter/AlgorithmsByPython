'''
Given a linked list, swap every two adjacent nodes and return its head.

For example,
Given 1->2->3->4, you should return the list as 2->1->4->3.

Your algorithm should use only constant space. You may not modify the values in the list, only nodes itself can be changed.
'''

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def swapPairs(self, head):
        if head == None or head.next == None:
            return head
        cur = head
        head = head.next
        while cur and cur.next:
            pNext = cur.next.next
            cur.next.next = cur
            if pNext:
                if pNext.next:
                    cur.next = pNext.next
                else:
                    cur.next = pNext
            else:
                cur.next = None
            cur = pNext
        return head
    # recursion
    def swapPairs2(self, head):
        if not head or not head.next:
            return head

        first, second = head, head.next
        third = second.next
        head = second
        second.next = first
        first.next = self.swapPairs(third)
        return head