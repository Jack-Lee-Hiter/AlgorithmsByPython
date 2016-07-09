'''
实现基数排序RadixSort, 分为:
最高位优先(Most Significant Digit first)法
最低位优先(Least Significant Digit first)法
'''

# 最低位优先法
def radixSortLSD(alist):
    if len(alist) == 0:
        return
    if len(alist) == 1:
        return alist
    tempList = alist
    maxNum = max(alist)
    radix = 10
    while maxNum * 10 > radix:
        newArr = [[], [], [], [], [], [], [], [], [], []]
        for n1 in tempList:
            testnum = n1 % radix
            testnum = testnum // (radix / 10)
            for n2 in range(10):
                if testnum == n2:
                    newArr[n2].append(n1)
        tempList = []
        for i in range(len(newArr)):
            for j in range(len(newArr[i])):
                tempList.append(newArr[i][j])
        radix *= 10
    return tempList



print(radixSortLSD([10, 12, 24, 23, 13, 52, 15, 158, 74, 32, 254, 201, 30, 19]))
