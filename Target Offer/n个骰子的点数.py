# -*- coding:UTF-8 -*-
'''
把n个骰子扔在地上, 所有骰子朝上一面的点数和为s。
输入n, 打印出s的所有可能的值出现的概率
'''
# 基于循环求点数, 时间性能好
def PrintProbability(number):
    if number < 1:
        return
    maxVal = 6
    # 构造两个数组来存储骰子点数的每一个总数出现的次数
    # 在一次循环中, 第一个数组中的第n个数字表示骰子和为n出现的次数
    # 在下次循环中, 另一个数组的第n个数字设为前一个数组对应的第n-1、n-2、n-3、n-4、n-5、n-6之和
    probStorage = [[], []]
    probStorage[0] = [0]*(maxVal * number + 1)
    flag = 0
    for i in range(1, maxVal+1):
        probStorage[flag][i] = 1
    for time in range(2, number+1):
        probStorage[1-flag] = [0]*(maxVal * number + 1)
        for pCur in range(time, maxVal*time+1):
            diceNum = 1
            while diceNum < pCur and diceNum <= maxVal:
                probStorage[1-flag][pCur] += probStorage[flag][pCur-diceNum]
                diceNum += 1
        flag = 1 - flag
    total = maxVal ** number
    for i in range(number, maxVal*number+1):
        ratio = probStorage[flag][i] / float(total)
        print("{}: {:e}".format(i, ratio))
s = PrintProbability(5)