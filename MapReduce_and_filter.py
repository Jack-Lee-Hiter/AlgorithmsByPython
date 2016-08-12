# -*- coding:UTF-8 -*-
import functools
# Python3.x和Python2.x对于map、reduce、filter的处理变得不同
# Python3.x中map和filter的输出是一个map型和filter型, 需要从里面取出需要的值
# Python2.x中map和filter输出的直接是一个list
# Python3.x中使用reduce需要引入functools

# 使用map把list中的int变为str
map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9])
# 使用map()把名字规范化, 首字母大写,其余小写
def standardName(s):
    return s.capitalize()
print([x for x in map(standardName, ['adam', 'LISA', 'barT'])])
# 在Python2.x中应该使用print(map(standardName, ['adam', 'LISA', 'barT']))

# 使用reduce()输出一个list的所有数的乘积
def prod(aList):
    return functools.reduce(lambda x, y: x*y, aList)
print(prod([1, 2, 3, 4, 5]))

# 使用filter()打印100以内的素数
def isPrime(n):
    isPrimeFlag = True
    if n <= 1:
        isPrimeFlag = False
    i = 2

    while i * i <= n:
        if n % i == 0:
            isPrimeFlag = False
            break
        i += 1
    return n if isPrimeFlag else None
print(filter(isPrime, range(101)))