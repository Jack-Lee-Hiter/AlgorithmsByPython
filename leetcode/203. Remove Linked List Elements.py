'''
Remove all elements from a linked list of integers that have value val.
Example
Given: 1 --> 2 --> 6 --> 3 --> 4 --> 5 --> 6, val = 6
Return: 1 --> 2 --> 3 --> 4 --> 5
'''
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    
    def removeElements(self, head, val):
        preNode, res = None, head
        while head:
            if head.val == val:
                if not preNode:
                    res = res.next
                else:
                    preNode.next = head.next
            else:
                preNode = head
            head = head.next
        return res