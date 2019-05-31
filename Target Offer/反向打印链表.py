'''
输入一个链表，从尾到头打印链表每个节点的值。
'''
class ListNode:
    def __init__(self, x=None):
        self.val = x
        self.next = None

class Solution:
    def printListFromTailToHead(self, listNode):
        if listNode.val == None:
            return
        l = []
        head = listNode
        while head:
            l.insert(0, head.val)
            head = head.next
        return l

# 添加使用递归调用的方法，堆栈和递归是一样的
    def recursive(self, listNode):  
        if listNode.val != None:
            if listNode.next != None:
                self.recursive(listNode.next)
                
            print(listNode.val)


node1 = ListNode(10)
node2 = ListNode(11)
node3 = ListNode(13)
node1.next = node2
node2.next = node3

singleNode = ListNode(12)

test = ListNode()

S = Solution()
print(S.printListFromTailToHead(node1))
print(S.printListFromTailToHead(test))
print(S.printListFromTailToHead(singleNode))
