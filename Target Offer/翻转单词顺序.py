'''
输入一个英文句子, 翻转句子中单词的顺序,但单词内字符的顺序不变
为简单起见, 标点符号和普通字母一样处理
'''

# -*- coding:utf-8 -*-
class Solution:
    # 按照书上的方法进行编写
    # 因为Python的字符串结束没有结束符, 所以需要判断最后的pEnd是否已经指到最后一个字符
    # 如果已经指到最后一个字符, 则直接在复制之后跳出循环
    # 测试用例'I am a student.'和' '和''
    def ReverseSentence(self, s):
        if s == None or len(s) <= 0:
            return ''
        strList = list(s)
        strList = self.Reverse(strList)
        pBegin = 0
        pEnd = 0
        resultStr = ''
        listTemp = []

        while pEnd < len(s):
            # 如果字符串长度为1, 直接跳出循环
            # 如果pEnd指针指到最后一个字符, 跳出循环
            if pEnd == len(s)-1:
                listTemp.append(self.Reverse(strList[pBegin:]))
                break
            # 这个判断语句位置需要靠前, 用来鉴定字符串开头是否是空格的情况
            if strList[pBegin] == ' ':
                pBegin += 1
                pEnd += 1
                listTemp.append(' ')
            elif strList[pEnd] == ' ':
                listTemp.append(self.Reverse(strList[pBegin:pEnd]))
                pBegin = pEnd
            else:
                pEnd += 1
        # print(listTemp)
        for i in listTemp:
            resultStr += ''.join(i)
        return resultStr
    # 翻转字符list
    def Reverse(self, alist):
        if alist == None or len(alist) <= 0:
            return ''
        startIndex = 0
        endIndex = len(alist) - 1
        while startIndex < endIndex:
            alist[startIndex], alist[endIndex] = alist[endIndex], alist[startIndex]
            startIndex += 1
            endIndex -= 1
        return alist

    # 直接利用Python的语句进行字符串的翻转
    def ReverseSentence2(self, s):
        l = s.split(' ')
        return ' '.join(l[::-1])


str = 'I am a student.'
s = Solution()
print(s.ReverseSentence2(str))