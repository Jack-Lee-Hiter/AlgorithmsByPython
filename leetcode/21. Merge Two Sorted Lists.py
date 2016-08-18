'''
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.
'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        if l1 == None or l2 == None:
            return l1 or l2
        pHead = pNode = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                pNode.next = l1
                l1 = l1.next
            else:
                pNode.next = l2
                l2 = l2.next
            pNode = pNode.next
        pNode.next = l1 or l2
        return pHead.next
    # recursively
    def mergeTwoLists2(self, l1, l2):
        if not l1 or not l2:
            return l1 or l2
        if l1.val < l2.val:
            l1.next = self.mergeTwoLists2(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists2(l1, l2.next)
            return l2
    