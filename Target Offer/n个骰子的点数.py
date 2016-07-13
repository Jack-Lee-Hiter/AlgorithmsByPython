'''
把n个骰子扔在地上, 所有骰子朝上一面的点数和为s。
输入n, 打印出s的所有可能的值出现的概率
'''
# 基于循环求点数, 时间性能好
def PrintProbability(number):
    if number < 1:
        return
    maxValue = 6
    # 构造两个数组来存储骰子点数的每一个总数出现的次数
    # 在一次循环中, 第一个数组中的第n个数字表示骰子和为n出现的次数
    # 在下次循环中, 另一个数组的第n个数字设为前一个数组对应的第n-1、n-2、n-3、n-4、n-5、n-6之和
    probabilities = [[], []]
    probabilities[0] = [0]*(maxValue * number + 1)
    probabilities[1] = [0]*(maxValue * number + 1)
    flag = 0
    for i in range(1, maxValue+1):
        probabilities[flag][i] = 1
    for k in range(2, number+1):
        for i in range(k):
            probabilities[1-flag][i] = 0
        for i in range(k, maxValue*k+1):
            probabilities[1-flag][i] = 0
            j = 1
            while j < i and j <= maxValue:
                probabilities[1-flag][i] += probabilities[flag][i-j]
                j += 1
        flag = 1 - flag
    total = maxValue ** number
    for i in range(number, maxValue*number+1):
        ratio = probabilities[flag][i] / total
        print("%d: %e" % (i, ratio))
s = PrintProbability(11)