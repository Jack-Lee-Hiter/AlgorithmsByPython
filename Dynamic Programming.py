# 解决动态规划中的找零问题
# 输入需要找零的金额和货币的币值向量
# 输出满足找零条件的最少的硬币个数
def ChangeMaking(coinValueList, change):
    alist = [0]*(change+1)
    for i in range(1, change+1):
        temp = change; j = 0
        while j <= len(coinValueList)-1 and i >= coinValueList[j]:
            temp = min(alist[i-coinValueList[j]], temp)
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