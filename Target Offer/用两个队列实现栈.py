# -*- coding:UTF-8 -*-
'''
两个队列实现栈
'''
class Solution:
    def __init__(self):
        self.queue1 = []
        self.queue2 = []
        
    def push(self, nNode):
        if self.queue2 == []:
            self.queue1.append(nNode)
        else:
            self.queue2.append(nNode)
 
 # 如果队列1中有值，那么就把队列1中的值除最后一个外全部清空，只留下最后一个弹出
    # 同样的道理，队列1清空，队列2有值，那么弹出的时候，就把队列2中除最后一个元素外全部加入队列1，队列2最后一个元素弹出
    def pop(self):
        if len(self.queue1) == 0 and len(self.queue2) == 0:
            return 
        else:
            if self.queue1 != []:
                while len(self.queue1) > 1:
                    self.queue2.append(self.queue1.pop(0))
                return self.queue1.pop()
            
            else:
                while(self.queue2) > 1:
                    self.queue1.append(self.queue2.pop(0))
                return self.queue2

P = Solution()
P.push(10)
P.push(11)
P.push(12)
print(P.pop())
P.push(13)
print(P.pop())
print(P.pop())
print(P.pop())
print(P.pop())
