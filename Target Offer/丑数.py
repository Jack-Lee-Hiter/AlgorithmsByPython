'''
把只包含因子2、3和5的数称作丑数（Ugly Number）。例如6、8都是丑数，但14不是，因为它包含因子7。
习惯上我们把1当做是第一个丑数。求按从小到大的顺序的第N个丑数。
'''

# -*- coding:utf-8 -*-
class Solution:
    def GetUglyNumber_Solution(self, index):
        if index == None and len(index) <= 0:
            return 0

        uglyNumbers = [1]*index
        nextIndex = 1

        index2 = 0
        index3 = 0
        index5 = 0

        while nextIndex < index:
            minVal = min(uglyNumbers[index2]*2, uglyNumbers[index3]*3, uglyNumbers[index5]*5)
            uglyNumbers[nextIndex] = minVal

            while uglyNumbers[index2]*2 <= uglyNumbers[nextIndex]:
                index2 += 1
            while uglyNumbers[index3]*3 <= uglyNumbers[nextIndex]:
                index3 += 1
            while uglyNumbers[index5]*5 <= uglyNumbers[nextIndex]:
                index5 += 1
            nextIndex += 1

        return uglyNumbers[-1]


s = Solution()
print(s.GetUglyNumber_Solution(11))

# def getUglyNumber(index):
#     if index <= 0:
#         return 0
#
#     uglyNumbers = [1] * index
#     nextUglyIndex = 1
#
#     index2 = 0
#     index3 = 0
#     index5 = 0
#     multiply2 = uglyNumbers[index2]
#     multiply3 = uglyNumbers[index3]
#     multiply5 = uglyNumbers[index5]
#
#     while nextUglyIndex < index:
#         minVal = min(multiply2 * 2, multiply3 * 3, multiply5 * 5)
#         uglyNumbers[nextUglyIndex] = minVal
#
#         while multiply2 * 2 <= uglyNumbers[nextUglyIndex]:
#             index2 += 1
#             multiply2 = uglyNumbers[index2]
#         while multiply3 * 3 <= uglyNumbers[nextUglyIndex]:
#             index3 += 1
#             multiply3 = uglyNumbers[index3]
#         while multiply5 * 5 <= uglyNumbers[nextUglyIndex]:
#             index5 += 1
#             multiply5 = uglyNumbers[index5]
#
#         nextUglyIndex += 1
#     return uglyNumbers[-1]