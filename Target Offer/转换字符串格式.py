'''
转换字符串格式为原来字符串里的字符+该字符连续出现的个数
例如1233422222, 转化为1121324125
'''

def convertString(string):
    if string == None or len(string) <= 0:
        return
    outputStr = ""
    length = len(string)
    index = 0
    while index < length:
        count = 0
        while index+count < length and string[index] == string[index+count]:
            count += 1
        outputStr += string[index] + str(count)
        index += count
    return outputStr

# 可以用来判断字符串标识的函数, 比如Mississippi转化为"i4m1p2s4"
# 这里讲次数出现1次的省去, Mississippi转化为"mi4s4p2"
def convertString2(string):
    if string == None or len(string) <= 0:
        return
    string.lower()
    outputStr = ""
    dictSet = {}
    for i in string:
        if i not in dictSet.keys():
            dictSet[i] = 0
        dictSet[i] += 1
    for i in string:
        if i in outputStr: continue
        outputStr += (i + str(dictSet[i])) if dictSet[i] != 1 else i
    return outputStr

print(convertString("1233422222"))
print(convertString("a"))
print(convertString2("mississippi"))
