# -*- coding:UTF-8 -*-
'''
实现BM算法, 算法质量介于KMP和Sunday之间
'''
def BoyerMoore(original, pattern):
    if original == None or pattern == None or len(original) < len(pattern):
        return None
    len1, len2 = len(original), len(pattern)
    pAppear = []
    # 查找一个字符使用蛮力法即可
    if len2 == 1:
        for i in range(len1):
            if original[i] == pattern[0]:
                pAppear.append(i)
    else:
        badTable = badCharTable(pattern)
        goodTable = goodSuffixTable(pattern)
        index = len2 - 1
        while index < len1:
            indexOfP = len2 - 1
            while index < len1 and pattern[indexOfP] == original[index]:
                if indexOfP == 0:
                    pAppear.append(index)
                    index += len2 + 1
                    indexOfP += 1
                    continue
                index -= 1
                indexOfP -= 1
            if index < len1:
                index += max(goodTable[len2 - 1 - indexOfP], badTable[original[index]])
    return pAppear if pAppear else False
'''
生成一个坏字符表, 移动距离分为两种
字符不在模式中, 移动的长度为模式的长度;
字符在模式中,移动的长度为模式中最右边对应待检测字符对应的模式中存在的此字符到最后一个字符的距离
对于BARBER，除了E,B,R,A的单元格分别为1，2，3，4之外，所有字符移动的单元格均为6
'''
def badCharTable(pattern):
    table = {}
    length = len(pattern)
    alphaBet = list(map(chr, range(32, 127)))   # 利用map生成一个原始移动表, 对应字符为从SPACE到~, 使用UTF-8对应表
    for i in alphaBet:
        table[i] = length
    # 更改pattern中存在字符的对应移动距离
    for j in range(length-1):
        table[pattern[j]] = length - 1 - j
    return table

'''
生成一个好后缀表
'''
def goodSuffixTable(pattern):
    length = len(pattern)
    tabel = [0] * length
    lastPrefixPosition, i = len(pattern), length - 1
    while i >= 0:
        if isPrefix(pattern, i):
            lastPrefixPosition = i
        tabel[length - 1 - i] = lastPrefixPosition - i + length - 1
        i -= 1
    for i in range(length-1):
        slen = suffixLength(pattern, i)
        tabel[slen] = length - 1 - i + slen
    return tabel
'''
判断模式后面几个字符是否等于模式前面相应长度的字符
'''
def isPrefix(pattern, p):
    length, j = len(pattern), 0
    for i in range(p, length):
        if pattern[i] != pattern[j]:
            return False
        j += 1
    return True
'''
判断前缀以及后缀的重复长度
'''
def suffixLength(pattern, p):
    length, samLen = len(pattern), 0
    i, j = p, length-1
    while i >= 0 and pattern[i] == pattern[j]:
        samLen += 1
        i -= 1
        j -= 1
    return samLen
print(BoyerMoore('aaaaa', 'aa'))