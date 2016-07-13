'''
随机从扑克牌中抽出了5张牌,判断是不是顺子,
决定大\小 王可以看成任何数字,并且A看作1,J为11,Q为12,K为13。
'''

# -*- coding:utf-8 -*-
class Solution:
    def IsContinuous(self, numbers):
        if numbers == None or len(numbers) <= 0:
            return False
        # 把A、J、Q、K转化一下
        transDict = {'A': 1, 'J': 11, 'Q': 12, 'K': 13}
        for i in range(len(numbers)):
            if numbers[i] in transDict.keys():
                numbers[i] = transDict[numbers[i]]

        numbers = sorted(numbers)
        numberOfzero = 0
        numberOfGap = 0

        # 统计0的个数
        i = 0
        while i < len(numbers) and numbers[i] == 0:
            numberOfzero += 1
            i += 1
        # 统计间隔的数目
        small = numberOfzero
        big = small + 1
        while big < len(numbers):
            # 出现对子, 不可能是顺子
            if numbers[small] == numbers[big]:
                return False

            numberOfGap += numbers[big] - numbers[small] - 1
            small = big
            big += 1
        return False if numberOfGap > numberOfzero else True

test = ['A', 3, 2, 5, 0]
test2 = [0, 3, 1, 6, 4]
s = Solution()
print(s.IsContinuous(test2))