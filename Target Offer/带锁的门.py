'''
走廊上有n个带锁的门,从1到n依次编号。最初所有的门都是关着的。我们从门前经过n次,每次都是从1号门开始。
在第i次经过的时候改变第i个整数倍号所的状态。
在最后一次经过的后, 哪些门是打开的, 输出打开门的序号
'''

def openDoor(n):
    if n == None or n <= 0:
        return
    doorList = [0] * (n+1)
    for i in range(1, len(doorList)):
        j = i
        while j <= n:
            doorList[j] = 1 - doorList[j]
            j += i
    output = [i for i, x in enumerate(doorList) if x != 0]
    return output

print(openDoor(16))
