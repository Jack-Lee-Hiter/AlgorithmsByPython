'''
零钱找零问题，使用动态规划
'''
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

'''
零钱找零问题的进阶
美团笔试题
给你六中零钱1,5,10,20,50,100的纸币，给定一个金额，写出所有可能的找零的个数
输入2，输出1；输入5，输出2
也是使用动态规划
'''
import sys
try:
    while True:
        line = sys.stdin.readline().strip()
        if line == '':
            break
        target = int(line)
        coinVal = [1, 5, 10, 20, 50, 100]
        alist = [0]*(target+1)
        alist[0] = 1
        for i in range(6):
            j = coinVal[i]
            while j <= target:
                alist[j] = alist[j] + alist[j-coinVal[i]]
                j += 1
        print(alist[-1])
except:
    pass
