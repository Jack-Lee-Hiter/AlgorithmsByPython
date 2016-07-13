'''
写一个函数，求两个整数之和，要求在函数体内不得使用+、-、*、/四则运算符号。
'''
# 利用异或以及与进位求解
# 不能一个正数一个负数
# 可能是python的的整型可以无限大的原因, 导致正数和负数的异或操作不断变成更小的负数而不会溢出
# 使用Swift尝试了一下, 还是可以求得正数和负数的位操作相加运算的
# -*- coding:utf-8 -*-
class Solution:
    def Add(self, num1, num2):
        while num2:
            sum = num1 ^ num2
            carry = (num1 & num2) << 1
            num1 = sum
            num2 = carry
        return num1
s = Solution()
print(s.Add(4, 2))
