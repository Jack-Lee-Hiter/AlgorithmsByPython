'''
输入一个整数, 输出不大于这个整数的所有连续的质数序列
认为1不是质数
'''

def Sieve(n):
    if n == None or n <= 1:
        return
    temp = [0]*(n+1)
    for p in range(2, len(temp)):
        temp[p] = p
    for p in range(2, int(n**0.5)+1):
        if temp[p] != 0:
            j = p * p
            while j <= n:
                temp[j] = 0
                j += p
    output = []
    for i in temp:
        if i != 0:
            output.append(i)
    return output

print(Sieve(29))