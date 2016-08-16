# -*- coding:utf-8 -*-
'''
给出两个字符串，找到最长公共子串，并返回其长度。
'''

class Solution:
    # 动态规划解决最长公共子串问题
    # 时间复杂度O(m*n), 空间复杂度O(m*n)
    def longestCommonSubstring(self, A, B):
        if A == None or B == None or len(A) + len(B) == 0:
            return 0
        lenA, lenB = len(A), len(B)
        C = [[0] * (lenB+1) for i in range(lenA + 1)]
        maxLen, maxIndex = 0, 0
        for i in range(1, lenA + 1):
            for j in range(1, lenB + 1):
                if A[i-1] == B[j-1]:
                    C[i][j] = C[i-1][j-1] + 1
                    if C[i][j] > maxLen:
                        maxLen = C[i][j]
                        maxIndex = i - maxLen
        LCS = A[maxIndex:maxIndex + maxLen]
        return maxLen, LCS
    # 利用后缀数组解决最长公共子串问题
    def longestCommonSubstring2(self, A, B):
        if A == None or B == None:
            return
        s = A + "#" + B
        indexOfSharp = len(A)
        SA = self.suffixArray(s)
        maxLen, maxIndex = 0, 0
        hasCommon = False
        for i in range(len(s) - 1):
            diff = (SA[i] - indexOfSharp) * (SA[i + 1] - indexOfSharp)
            if diff < 0:
                tempLen = self.comlen(s, SA[i], SA[i + 1])
                if tempLen > maxLen:
                    maxLen = tempLen
                    maxIndex = SA[i]
                    hasCommon = True
        return (maxLen, s[maxIndex:maxIndex + maxLen]) if hasCommon else False
    # 得到一个字符串的后缀数组
    def suffixArray(self, s):
        if s == None or len(s) == 0:
            return None
        allSuffix = []
        for i in range(len(s)):
            allSuffix.append([s[i:], i])
        sortedList = sorted(allSuffix)
        SA = [w[1] for w in sortedList]
        return SA
    # 比较得到后缀数组中两个相邻的元素分别对应的后缀字符串的最长前缀
    def comlen(self, s, p, q):
        j = 0
        while j < len(s[p:]) and j < len(s[q:]) and s[p:p + j + 1] == s[q:q + j + 1]:
            j += 1
        return j

s = Solution()
print(s.longestCommonSubstring("acbabc", "acaccbabb"))
print(s.longestCommonSubstring2("acbabc", "acaccbabb"))


