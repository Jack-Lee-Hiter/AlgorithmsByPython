# -*- coding:utf-8 -*-
'''
给出 n，问由 1...n 为节点组成的不同的二叉查找树有多少种？
本质上是求得一个卡特兰数列
卡特兰数列递推公式: F(n) = C(2n, n)/(n+1) = (2n)!/( (n+1)! * n! )
1, 1, 2, 5, 14, 42, 132, 429, 1430, 4862, 16796, 58786, 208012, 742900, 2674440, 9694845, 35357670, 129644790, 477638700, 1767263190
'''


class Solution:
    def numTrees(self, n):
        # n为0的时候输出1
        if n == 0 or n == None:
            return 1
        return self.factorial(n << 1) // (self.factorial(n) * self.factorial(n + 1))
    # 定义一个函数求取n的阶乘
    def factorial(self, n):
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result

s = Solution()
print(s.numTrees(0))
print(s.numTrees(1))
print(s.numTrees(2))
print(s.numTrees(3))
print(s.numTrees(4))