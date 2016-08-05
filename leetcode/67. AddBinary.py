'''
Given two binary strings, return their sum (also a binary string).
For example,
a = "11"
b = "1"
Return "100".
'''
class Solution(object):
    def addBinary(self, a, b):
        lenA, lenB = len(a), len(b)
        a, b = list(a), list(b)
        if lenA == 0:
            return b
        if lenB == 0:
            return a
        carry, r = 0, ['']*(max(lenA, lenB)+1)
        for i in range(len(r)):
            p1, p2 = 0, 0
            if i < lenA:
                p1 = int(a[lenA-1-i])
            if i < lenB:
                p2 = int(b[lenB-1-i])
            sum = p1 + p2 + carry
            r[len(r)-1-i] = str(sum%2)
            carry = sum // 2
        return str(int("".join(r)))
s = Solution()
print(s.addBinary('10110', '101'))