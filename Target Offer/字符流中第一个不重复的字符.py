'''
请实现一个函数用来找出字符流中第一个只出现一次的字符。
例如，当从字符流中只读出前两个字符"go"时，第一个只出现一次的字符是"g"。
当从该字符流中读出前六个字符“google"时，第一个只出现一次的字符是"l"。
如果当前字符流没有存在出现一次的字符，返回#字符。
'''

# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.adict = {}
        self.alist = []
    def FirstAppearingOnce(self):
        while len(self.alist) > 0 and self.adict[self.alist[0]] == 2:
            self.alist.pop(0)
        if len(self.alist) == 0:
            return '#'
        else:
            return self.alist[0]
    def Insert(self, char):
        if char not in self.adict.keys():
            self.adict[char] = 1
            self.alist.append(char)
        elif self.adict[char]:
            self.adict[char] = 2