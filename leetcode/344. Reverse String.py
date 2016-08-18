'''
Write a function that takes a string as input and returns the string reversed.

Example:
Given s = "hello", return "olleh".
'''

class Solution(object):
    def reverseString(self, s):
        return s[::-1]
    def reverseString2(self, s):
        if not s or len(s) < 2:
            return s
        slist = list(s)
        start, end = 0, len(s)-1
        while start < end:
            slist[start], slist[end] = slist[end], slist[start]
            start += 1
            end -= 1
        return "".join(slist)

s = Solution()
print(s.reverseString("hello"))