'''
找出一行字符串中出现的相同且长度最长的字符串, 输出它及首字符的位置
例如"yyabcdabjcabceg", 输出结果应该为abc和3
'''

def maxStr(string):
    if string == None or len(string) <= 0:
        return
    if len(string) == 1:
        return [string, 0]
    length = len(string)
    temp = []
    for i in range(length):
        temp.append(string[i:])
    listWithIndex = []
    for index, val in enumerate(temp):
        listWithIndex.append([val, index+1])
    listWithIndex.sort()
    maxLength, maxList, maxIndex = 0, "", 0
    for listIndex in range(length-1):
        firstList = listWithIndex[listIndex]
        secondList = listWithIndex[listIndex+1]
        index, tempLength, tempList = 0, 0, ""
        while index < len(firstList[0]) and index < len(secondList[0]) and firstList[0][index] == secondList[0][index]:
            tempLength += 1
            tempList += firstList[0][index]
            index += 1
        if tempLength > maxLength:
            maxLength = tempLength
            maxList = tempList
            maxIndex = min(firstList[1], secondList[1])
    return [maxList, maxIndex]




print(maxStr("yyabcdabjcabceg"))
print(maxStr("abcbc"))