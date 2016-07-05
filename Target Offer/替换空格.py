'''
请实现一个函数，将一个字符串中的空格替换成“%20”。
例如，当字符串为We Are Happy.则经过替换之后的字符串为We%20Are%20Happy。
'''

# -*- coding:utf-8 -*-
class Solution:
    # s 源字符串

    # 创建新的字符串进行替换
    def replaceSpace1(self, s):
        tempstr = ''
        if type(s) != str:
            return
        for c in s:
            if c == ' ':
                tempstr += '%20'
            else:
                tempstr += c
        return tempstr

    # 简单代码替换
    def replaceSpace2(self, s):
        if type(s) != str:
            return
        return s.replace(' ', '%20')

    # 书中给的思路
    def replaceSpace3(self, s):
        if type(s) != str:
            return
        if len(s) <= 0:
            return
        spaceNum = 0
        for i in s:
            if i == " ":
                spaceNum += 1

        newStrLen = len(s) + spaceNum * 2
        newStr = newStrLen * [None]
        indexOfOriginal = len(s) - 1
        indexOfNew = newStrLen - 1
        while indexOfNew >= 0 and indexOfNew >= indexOfOriginal:
            if s[indexOfOriginal] == ' ':
                newStr[indexOfNew] = '0'
                newStr[indexOfNew-1] = '2'
                newStr[indexOfNew-2] = '%'
                indexOfNew -= 3
                indexOfOriginal -= 1
            else:
                newStr[indexOfNew] = s[indexOfOriginal]
                indexOfNew -= 1
                indexOfOriginal -= 1
        changedStr = ''
        for c in newStr:
            changedStr += c
        return changedStr


s = 'we are happy'
test = Solution()
print(test.replaceSpace1(s))
print(test.replaceSpace2(s))
print(test.replaceSpace3(s))
