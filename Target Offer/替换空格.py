'''
请实现一个函数，将一个字符串中的空格替换成“%20”。
例如，当字符串为We Are Happy.则经过替换之后的字符串为We%20Are%20Happy。
'''

# -*- coding:utf-8 -*-
class Solution:
    # s 源字符串
    
    # 使用append一次遍历即可替换
    # 由于list的append是O(1)的时间复杂度，除了扩容所导致的时间损耗，该算法复杂度为O(n)
    def replaceSpaceByAppend(self, s):
        string = list(string)
	    stringReplace = []
	    for item in string:
		    if item == ' ':
			    stringReplace.append('%')
			    stringReplace.append('2')
			    stringReplace.append('0')
		    else:
			    stringReplace.append(item)
	    return "".join(stringReplace)

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
    # 在Python中str类型是不可变的类型, 使用replace语句会生成一个新的str, 原始的s还是带空格的str变量
    def replaceSpace2(self, s):
        if type(s) != str:
            return
        return s.replace(' ', '%20')

    # 书中给的思路
    # 判断输入类型的时候，isinstance必须首先判断，因为如果输入为integer的话，没有len，就会直接报错
    def replaceSpace3(self, s):
        if not isinstance(s,str) or len(s) <= 0 or s == None:
            return ""
        spaceNum = 0
        for i in s:
            if i == " ":
                spaceNum += 1

        newStrLen = len(s) + spaceNum * 2
        newStr = newStrLen * [None]
        indexOfOriginal, indexOfNew = len(s) - 1, newStrLen - 1
        while indexOfNew >= 0 and indexOfNew >= indexOfOriginal:
            if s[indexOfOriginal] == ' ':
                newStr[indexOfNew-2:indexOfNew+1] = ['%', '2', '0']
                indexOfNew -= 3
                indexOfOriginal -= 1
            else:
                newStr[indexOfNew] = s[indexOfOriginal]
                indexOfNew -= 1
                indexOfOriginal -= 1
        return "".join(newStr)


s = 'we are happy'
test = Solution()
print(test.replaceSpace1(s))
print(test.replaceSpace2(s))
print(test.replaceSpace3(s))
