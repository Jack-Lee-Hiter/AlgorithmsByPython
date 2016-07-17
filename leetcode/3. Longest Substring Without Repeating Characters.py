'''
Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
'''

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        if s == None or len(s) <= 0:
            return
        # charDict存储每个字符以及字符出现的最后的位置, res为当前最长的的子串长度, st当前无重复子串的最左边字符的位置
        charDict, res, st = {}, 0, 0
        for i, ch in enumerate(s):
            if ch not in charDict or charDict[ch] < st:
                res = max(res, i - st + 1)
            else:
                st = charDict[ch] + 1
            charDict[ch] = i
        return res

s = Solution()
print(s.lengthOfLongestSubstring('pwwkew'))