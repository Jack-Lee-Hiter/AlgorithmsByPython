'''
求一个字符串的最长子串，其中子串所有字符相同
面试题
'''
def findCommonLCS(s):
    if not s:
        return ""
    if len(s) == 1:
        return s
    length = len(s)
    maxIndex, maxLength = 0, 1
    curIndex = 0
    while curIndex < length:
        tempLength = 1
        while curIndex + tempLength < length and s[curIndex] == s[curIndex+tempLength]:
            tempLength += 1
        if maxLength < tempLength:
            maxLength = tempLength
            maxIndex = curIndex
        if curIndex + tempLength == length:
            break
        curIndex += tempLength
    if maxLength == 1:
        return s[0]
    else:
        res = s[maxIndex:maxIndex+maxLength]
        return res

print(findCommonLCS("abbbasagsagsgdsaagaaccagcfsccccc"))