'''
Given a string S, find the longest palindromic substring in S. You may assume that the maximum length of S is 1000, and there exists one unique longest palindromic substring.
'''

# 使用manacher算法进行字长回文串的判断
class Solution(object):
    def longestPalindrome(self, s):
        if s == None or len(s) <= 0:
            return
        newS = '#' + '#'.join(s) + '#'

        length, center, rightMost, maxCenter, maxLen, i = len(newS), 0, 0, 0, 0, 0
        pArr = [0] * length
        for i in range(length):
            pArr[i] = 1 if rightMost < i else min(rightMost-i, pArr[(center << 1) - i])
            while i + pArr[i] < length and i - pArr[i] > -1 and newS[i + pArr[i]] == newS[i - pArr[i]]:
                pArr[i] += 1
            if i + pArr[i] > rightMost:
                center = i
                rightMost = i + pArr[i]
                if pArr[i] > maxLen:
                    maxLen = pArr[i]
                    maxCenter = i
        start = (maxCenter - maxLen + 1) >> 1
        return s[start: start + maxLen - 1]

    def manacher(s):
        # 预处理
        s = '#' + '#'.join(s) + '#'

        RL = [0] * len(s)
        MaxRight = 0
        pos = 0
        MaxLen = 0
        for i in range(len(s)):
            if i < MaxRight:
                RL[i] = min(RL[2 * pos - i], MaxRight - i)
            else:
                RL[i] = 1
            # 尝试扩展，注意处理边界
            while i - RL[i] >= 0 and i + RL[i] < len(s) and s[i - RL[i]] == s[i + RL[i]]:
                RL[i] += 1
            # 更新MaxRight,pos
            if RL[i] + i - 1 > MaxRight:
                MaxRight = RL[i] + i - 1
                pos = i
            # 更新最长回文串的长度
            MaxLen = max(MaxLen, RL[i])
        return MaxLen - 1

test = 'aaaba'
s = Solution()
print(s.longestPalindrome(test))