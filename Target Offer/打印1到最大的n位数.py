'''
输入数字n, 按顺序打印从1最大的n位十进制数
比如输入3, 则打印出1、2、3、到最大的3位数即999
'''

def Print1ToMaxOfNDigits(n):
    if n <= 0:
        return

    number = ['0'] * n
    while not Increment(number):
        PrintNumber(number)

def Increment(number):
    isOverflow = False
    nTakeOver = 0
    nLength = len(number)

    for i in range(nLength-1, -1, -1):
        nSum = int(number[i]) + nTakeOver
        if i == nLength - 1:
            nSum += 1

        if nSum >= 10:
            if i == 0:
                isOverflow = True
            else:
                nSum -= 10
                nTakeOver = 1
                number[i] = str(nSum)
        else:
            number[i] = str(nSum)
            break

    return isOverflow

def PrintNumber(number):
    isBeginning0 = True
    nLength = len(number)

    for i in range(nLength):
        if isBeginning0 and number[i] != '0':
            isBeginning0 = False
        if not isBeginning0:
            print('%c' % number[i], end='')
    print('')
#
# Print1ToMaxOfNDigits(2)

def Print1ToMaxOfNDigits2(n):
    if n <= 0:
        return

    number = ['0'] * n
    for i in range(10):
        number[0] = str(i)
        Print1ToMaxOfNDigitsRecursively(number, n, 0)

def Print1ToMaxOfNDigitsRecursively(number, length, index):
    if index == length - 1:
        PrintNumber(number)
        return
    for i in range(10):
        number[index + 1] = str(i)
        Print1ToMaxOfNDigitsRecursively(number, length, index+1)

Print1ToMaxOfNDigits2(2)