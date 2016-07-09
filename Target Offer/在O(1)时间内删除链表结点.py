'''
给定单向链表的头指针和一个结点指针,定义一个函数在O(1)时间删除该结点
'''
class ListNode:
    def __init__(self, x=None):
        self.val = x
        self.next = None
    def __del__(self):
        self.val = None
        self.next = None

class Solution:
    def DeleteNode(self, pListHead, pToBeDeleted):
        if not pListHead or not pToBeDeleted:
            return None

        if pToBeDeleted.next != None:
            pNext = pToBeDeleted.next
            pToBeDeleted.val = pNext.val
            pToBeDeleted.next = pNext.next
            pNext.__del__()


        elif pListHead == pToBeDeleted:
            pToBeDeleted.__del__()
            pListHead.__del__()
        else:
            pNode = pListHead
            while pNode.next != pToBeDeleted:
                pNode = pNode.next
            pNode.next = None
            pToBeDeleted.__del__()


node1 = ListNode(10)
node2 = ListNode(11)
node3 = ListNode(13)
node4 = ListNode(15)
node1.next = node2
node2.next = node3
node3.next = node4

S = Solution()
S.DeleteNode(node1, node3)
print(node3.val)
S.DeleteNode(node1, node3)
print(node3.val)
print(node2.val)
S.DeleteNode(node1, node1)
print(node1.val)
S.DeleteNode(node1, node1)
print(node1.val)
