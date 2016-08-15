# -*- coding:UTF-8 -*-
'''
字符串匹配算法, 比KMP简单而且快, 比BM算法也简单
'''
def Sunday(str1, str2):
    if str1 == None or str2 == None or len(str1) < len(str2):
        return None
    len1, len2 = len(str1), len(str2)
    pAppear, moveDict = [], matchDict(list(str2))
    indexStr1 = 0
    while indexStr1 <= len1 - len2:
        indexStr2 = 0
        while indexStr2 < len2 and str1[indexStr1 + indexStr2] == str2[indexStr2]:
            indexStr2 += 1
        if indexStr2 == len2:
            pAppear.append(indexStr1)
            indexStr1 += len2
            continue
        if indexStr1 + len2 >= len1:
            break
        elif str1[indexStr1+len2] not in moveDict.keys():
            indexStr1 += len2 + 1
        else:
            indexStr1 += moveDict[str1[indexStr1+len2]]
    return pAppear if pAppear else False

def matchDict(aList):
    moveDict = {}
    length = len(aList)
    for i in range(length-1, -1, -1):
        if aList[i] not in moveDict.keys():
            moveDict[aList[i]] = length - i
    return moveDict

print(Sunday('aaaaa', 'aa'))