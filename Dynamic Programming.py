# 解决动态规划中的找零问题
# 输入需要找零的金额和货币的币值向量
# 输出满足找零条件的最少的硬币个数
def ChangeMaking(coinVal, change):
    alist = [0]*(change+1)
    for i in range(1, change+1):
        temp = change; j = 0
        while j <= len(coinVal)-1 and i >= coinVal[j]:
            temp = min(alist[i-coinVal[j]], temp)
            j += 1
        alist[i] = temp + 1
    return alist.pop()

print(ChangeMaking([1, 5, 10, 25], 63))

# 解决动态规划中的币值最大化问题---在满足所选硬币不相邻的条件下,从一堆硬币中选择最大金额的硬币
# 输入数组C[1..n]保存n个硬币的面值
# 输出可选硬币的最大金额
def coinRow(coinrow):
    alist = [0]*(len(coinrow)+1)
    alist[1] = coinrow[0]
    for i in range(2, len(coinrow)+1):
        alist[i] = max(coinrow[i-1]+alist[i-2], alist[i-1])
    return alist.pop()

print(coinRow([5, 1, 2, 10, 6, 2]))

# 解决0-1背包问题
def maxBag(weight, value, totalWeight):
    if len(weight) <= 0 or len(value) <= 0 or totalWeight <= 0 or len(weight) != len(value):
        return
    num = len(weight)
    tempMat = []
    for i in range(num+1):
        tempMat.append([0]*(totalWeight+1))
    for i in range(1, num+1):
        for j in range(1, totalWeight+1):
            if j - weight[i-1] >= 0:
                tempMat[i][j] = max(tempMat[i-1][j], value[i-1] + tempMat[i-1][j-weight[i-1]])
            else:
                tempMat[i][j] = tempMat[i-1][j]
    return tempMat[-1][-1]

weight, value, totalWeight = [2,1,3,2], [12,10,20,15], 5
print(maxBag(weight, value, totalWeight))