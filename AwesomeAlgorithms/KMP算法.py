# -*- coding:UTF-8 -*-
'''
实现KMP算法
'''
def kmp(str1, str2):
    if str1 == None or str2 == None or len(str1) < len(str2):
        return False
    index = 0                           # index为str2对应于每次开始的位置
    len1, len2 = len(str1), len(str2)
    moveTable = matchTable(list(str2))
    pAppear = []
    while index <= len1 - len2:
        tmpIndex = 0                    # tmpIndex为str2中字符走到的位置
        while tmpIndex < len2 and str1[index+tmpIndex] == str2[tmpIndex]:
            tmpIndex += 1
        if tmpIndex == len2:
            pAppear.append(index)
            index += len2
            continue
        elif tmpIndex > 0:
            index += tmpIndex - moveTable[tmpIndex-1]
        else:
            index += 1
    return pAppear if pAppear else False

# 生成KMP匹配表, 该表和next表不一样
def matchTable(aList):
    length = len(aList)
    table = [0]*length
    index = 1
    while index < length:
        sameLen = 0
        while aList[:sameLen+1] == aList[index:index+sameLen+1]:
            sameLen += 1
            table[index+sameLen-1] = sameLen
        if sameLen != 0:
            index += sameLen
        else:
            index += 1
    return table
# 更具有一般性的字符移动表
def matchTable2(aList):
    length = len(aList)
    table = [0]*length
    index = 1
    while index < length:
        sameLen = 0
        while index+sameLen < length and aList[sameLen] == aList[index+sameLen]:
            sameLen += 1
            table[index+sameLen-1] = sameLen
        if sameLen != 0:
            index += sameLen
        else:
            index += 1
    return table

print(kmp('aaaaa', 'aa'))
