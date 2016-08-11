'''
找出所有和为S的连续正数序列
输出所有和为S的连续正数序列。序列内按照从小至大的顺序，序列间按照开始数字从小到大的顺序
'''
class Solution:
    def FindContinuousSequence(self, tsum):
        if tsum < 3:
            return []
        small = 1
        big = 2
        middle = (tsum + 1) // 2
        curSum = small + big
        output = []
        while small < middle:
            if curSum == tsum:
                output.append(list(range(small, big+1)))
            while curSum > tsum and small < middle:
                curSum -= small
                small += 1
                if curSum == tsum:
                    output.append(list(range(small, big+1)))
            big += 1
            curSum += big
        return output

    def FindContinuousSequence2(self, tsum):
        if tsum < 3:
            return []
        small, big = 1, 2
        middle = (tsum + 1) >> 1
        curSum = small + big
        output = []
        while small < middle:
            if curSum == tsum:
                output.append(list(range(small, big + 1)))
                big += 1
                curSum += big
            elif curSum > tsum:
                curSum -= small
                small += 1
            else:
                big += 1
                curSum += big
        return output
s = Solution()
print(s.FindContinuousSequence2(15))