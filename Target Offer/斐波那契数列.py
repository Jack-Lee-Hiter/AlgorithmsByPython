'''
大家都知道斐波那契数列，现在要求输入一个整数n，请你输出斐波那契数列的第n项。
n<=39
'''

# -*- coding:utf-8 -*-
class Solution:
    def Fibonacci(self, n):
        tempArray = [0, 1]
        if n >= 2:
            for i in range(2, n+1):
                tempArray[i%2] = tempArray[0] + tempArray[1]
        return tempArray[n%2]
    # 青蛙跳台阶, 每次可以跳1级或2级
    def jumpFloor(self, number):
        # write code here
        tempArray = [1, 2]
        if number >= 3:
            for i in range(3, number + 1):
                tempArray[(i + 1) % 2] = tempArray[0] + tempArray[1]
        return tempArray[(number + 1) % 2]

    def jumpFloorII(self, number):
        ans = 1
        if number >= 2:
            for i in range(number-1):
                ans = ans * 2
        return ans

test = Solution()
print(test.Fibonacci(100))
print(test.jumpFloor(3))
print(test.jumpFloorII(2))