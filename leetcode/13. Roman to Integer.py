# -*- coding:utf-8 -*-
'''
Given a roman numeral, convert it to an integer.

Input is guaranteed to be within the range from 1 to 3999.

'''

class Solution(object):
    def romanToInt(self, s):
        romanDict = {'M':1000, 'D':500, 'C':100, 'L':50, 'X':10, 'V':5, 'I':1}
        res, p = 0, 'I'
        for ch in s[::-1]:
            if romanDict[ch] < romanDict[p]:
                res = res - romanDict[ch]
            else:
                res = res + romanDict[ch]
            p = ch
        return res

s = Solution()
print((s.romanToInt("IX")))