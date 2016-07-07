'''
输入一个整数，输出该数二进制表示中1的个数。其中负数用补码表示。
'''

class Solution:
    def NumberOf1(self, n):
        count = 0
        if n < 0:
            n = n & 0xffffffff
        while n:
            count += 1
            n = (n-1)&n
        return count

    def NumberOf2(self, n):
        if n < 0:
            s = bin(n & 0xffffffff)
        else:
            s = bin(n)
        return s.count('1')

    # 判断一个数是不是2得整数次幂
    def powerOf2(self, n):
        if n&(n-1) == 0:
            return True
        else:
            return False
    # 判断两个数的二进制表示有多少位不一样, 直接比较两个数的二进制异或就可以
    def andOr(self, m, n):
        diff = m^n
        count = 0
        while diff:
            count += 1
            diff = diff&(diff-1)
        return count

S = Solution()
print(S.NumberOf1(-1))
print(S.NumberOf2(-1))
print(S.powerOf2(64))
print(S.powerOf2(63))
print(S.andOr(10, 13))