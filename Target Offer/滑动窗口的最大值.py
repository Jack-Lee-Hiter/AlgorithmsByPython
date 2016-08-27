'''
给定一个数组和滑动窗口的大小，找出所有滑动窗口里数值的最大值。
例如，如果输入数组{2,3,4,2,6,2,5,1}及滑动窗口的大小3，那么一共存在6个滑动窗口，
他们的最大值分别为{4,4,6,6,6,5}；
针对数组{2,3,4,2,6,2,5,1}的滑动窗口有以下6个：
{[2,3,4],2,6,2,5,1}， {2,[3,4,2],6,2,5,1}， {2,3,[4,2,6],2,5,1}， {2,3,4,[2,6,2],5,1}， {2,3,4,2,[6,2,5],1}， {2,3,4,2,6,[2,5,1]}。
'''

# -*- coding:utf-8 -*-
class Solution:
    def maxInWindows(self, num, size):
        if not num or size <= 0:
            return []
        deque = []
        if len(num) >= size:
            index = []
            for i in range(size):
                while len(index) > 0 and num[i] > num[index[-1]]:
                    index.pop()
                index.append(i)

            for i in range(size, len(num)):
                deque.append(num[index[0]])
                while len(index) > 0 and num[i] >= num[index[-1]]:
                    index.pop()
                if len(index) > 0 and index[0] <= i - size:
                    index.pop(0)
                index.append(i)

            deque.append(num[index[0]])
        return deque

test = [2, 3, 4, 2, 6, 2, 5, 1]
s = Solution()
print(s.maxInWindows(test, 3))

