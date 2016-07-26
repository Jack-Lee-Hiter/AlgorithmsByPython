'''
在一组数的编码中，若任意两个相邻的代码只有一位二进制数不同， 则称这种编码为格雷码(Gray Code)，请编写一个函数，使用递归的方法生成N位的格雷码。
给定一个整数n，请返回n位的格雷码，顺序为从0开始。
'''

# -*- coding:utf-8 -*-

class GrayCode:
    def getGray(self, n):
        L, L1, L2 = [], [], []
        if n == 1:
            L = ['0', '1']
        else:
            L1 = self.getGray(n-1)
            L2 = L1[::-1]
            num = len(L1)
            for i in range(num):
                L1[i] = '0' + L1[i]
                L2[i] = '1' + L2[i]
            L = L1 + L2
        return L
s = GrayCode()
print(s.getGray(3))