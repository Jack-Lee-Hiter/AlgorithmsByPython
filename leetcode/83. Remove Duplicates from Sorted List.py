'''
Given a sorted linked list, delete all duplicates such that each element appear only once.

For example,
Given 1->1->2, return 1->2.
Given 1->1->2->3->3, return 1->2->3.
'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        pNode = head
        while pNode:
            while pNode.next and pNode.next.val == pNode.val:
                pNode.next = pNode.next.next
            pNode = pNode.next
        return head