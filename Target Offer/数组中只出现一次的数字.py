'''
一个整型数组里除了两个数字之外，其他的数字都出现了两次。请写程序找出这两个只出现一次的数字。
'''

# -*- coding:utf-8 -*-
class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        if array == None or len(array) <= 0:
            return []
        resultExclusiveOr = 0
        for i in array:
            resultExclusiveOr ^= i

        indexOf1 = self.FindFirstBitIs1(resultExclusiveOr)
        num1 = 0
        num2 = 0
        for j in range(len(array)):
            if self.IsBit1(array[j], indexOf1):
                num1 ^= array[j]
            else:
                num2 ^= array[j]
        return [num1, num2]

    def FindFirstBitIs1(self, num):
        indexBit = 0
        while num & 1 == 0 and indexBit <= 32:
            indexBit += 1
            num = num >> 1
        return indexBit

    def IsBit1(self, num, indexBit):
        num = num >> indexBit
        return num & 1

aList = [2, 4, 3, 6, 3, 2, 5, 5]
s = Solution()
print(s.FindNumsAppearOnce(aList))