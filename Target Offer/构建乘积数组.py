'''
给定一个数组A[0,1,...,n-1],请构建一个数组B[0,1,...,n-1]
其中B中的元素B[i]=A[0]*A[1]*...*A[i-1]*A[i+1]*...*A[n-1]。不能使用除法。
'''

# -*- coding:utf-8 -*-
class Solution:
    def multiply(self, A):
        if A == None or len(A) <= 0:
            return
        length = len(A)
        aList = [1] * length
        for i in range(1, length):
            aList[i] = aList[i-1] * A[i-1]
        temp = 1
        for i in range(length-2, -1, -1):
            temp = temp * A[i+1]
            aList[i] *= temp
        return aList

test = [1, 2, 3, 4]
s = Solution()
print(s.multiply(test))