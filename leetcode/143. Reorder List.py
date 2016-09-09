'''
Given a singly linked list L: L0→L1→…→Ln-1→Ln,
reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

You must do this in-place without altering the nodes' values.

For example,
Given {1,2,3,4}, reorder it to {1,4,2,3}.
'''


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reorderList(self, head):
        if not head or not head.next:
            return
        ahead, behind = self.split(head)
        behind = self.reverse(behind)
        head = self.reConnect(ahead, behind)
    # split the linkedlist in middle
    def split(self, head):
        fast = head
        slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next
            fast = fast.next
        middle = slow.next
        slow.next = None
        return head, middle
    # reverse the behind half linkedlist
    def reverse(self, head):
        reHead = None
        curNode = head
        while curNode:
            nextNode = curNode.next
            curNode.next = reHead
            reHead = curNode
            curNode = nextNode
        return reHead
    # merge the two linkedlist to one
    def reConnect(self, first, second):
        head = first
        tail = first
        first = first.next
        while second:
            tail.next = second
            tail = tail.next
            second = second.next
            if first:
                first, second = second, first
        return head