# 递归求和
def listSum(numlist):
    if len(numlist) == 1:
        return numlist[0]
    else:
        return numlist[0] + listSum(numlist[1:])

print(listSum([1, 2, 3, 4, 5, 6, 7]))

# 递归求阶乘
def listFactorial(num):
    if num <= 1:
        return 1
    else:
        return num * listFactorial(num-1)

print(listFactorial(10))

# 递归实现进制转换:
def toStr(n,base):
   convertString = "0123456789ABCDEF"
   if n < base:
      return convertString[n]
   else:
      return toStr(n//base, base) + convertString[n%base]

print(toStr(1453, 16))

# 递归实现Hanoi塔
def Hanoi(fromPole, withPole, toPole, diskNum):
    if diskNum <= 1:
        print("moving disk from %s to %s" % (fromPole, toPole))
    else:
        Hanoi(fromPole, toPole, withPole, diskNum-1)
        print("moving disk from %s to %s" % (fromPole, toPole))
        Hanoi(withPole, fromPole, toPole, diskNum-1)

Hanoi('A', 'B', 'C', 3)
