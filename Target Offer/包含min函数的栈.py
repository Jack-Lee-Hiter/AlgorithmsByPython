'''
定义栈的数据结构，请在该类型中实现一个能够得到栈最小元素的min函数。
'''

# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.stack = []
        self.minStack = []
    def push(self, node):
        self.stack.append(node)
        if self.minStack == [] or node < self.min():
            self.minStack.append(node)
        else:
            temp = self.min()
            self.minStack.append(temp)

    def pop(self):
        if self.stack == [] or self.minStack == []:
            return None
        self.minStack.pop()
        self.stack.pop()

    def top(self):
        return self.stack[-1]
    def min(self):
        return self.minStack[-1]

S = Solution()
S.push(3)
S.push(4)
S.push(2)
S.push(1)
print(S.min())
S.pop()
print(S.min())
S.pop()
print(S.min())