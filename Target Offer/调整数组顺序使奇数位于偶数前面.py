'''
输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有的奇数位于数组的前半部分
所有的偶数位于位于数组的后半部分，并保证奇数和奇数，偶数和偶数之间的相对位置不变。
'''


class Solution:
    # 一个类似于快排的方法, 只是简单的满足了奇数在前,偶数在后, 奇数的顺序发生了改变
    def reOrderArray(self, array):
        if len(array) < 1:
            return
        elif len(array) == 1:
            return array

        front = 0
        rear = len(array)-1
        while front <= rear:
            while array[front] & 0x1 == 1:
                front += 1
            while array[rear] & 0x1 == 0:
                rear -= 1
            array[front], array[rear] = array[rear], array[front]
        array[front], array[rear] = array[rear], array[front]
        return array
    # 直接利用Python的trick, 写一个简单的排列数组, 顺序不变
    def reOrderArray2(self, array):
        left = [x for x in array if x & 1]
        right = [x for x in array if not x & 1]
        return left + right

    def reOrderArray3(self, array):
        if len(array) < 1:
            return []
        if len(array) == 1:
            return array
        arrayOdd = []
        arrayEven = []
        for num in array:
            if num & 0x1:
                arrayOdd.append(num)
            else:
                arrayEven.append(num)
        return arrayOdd+arrayEven

    # 可扩展性的解法
    # 注意在一个函数的输入中, 输入另一个函数的写法func = self.fucName, funcName不需要加括号
    def Reorder(self, pData, length, func):
        if length == 0:
            return

        pBegin = 0
        pEnd = length - 1

        while pBegin < pEnd:
            while pBegin < pEnd and not func(pData[pBegin]):
                pBegin += 1
            while pBegin < pEnd and func(pData[pEnd]):
                pEnd -= 1

            if pBegin < pEnd:
                pData[pBegin], pData[pEnd] = pData[pEnd], pData[pBegin]
        return pData

    def isEven(self, n):
        return not n & 0x1

    def isNegtive(self, n):
        return n >= 0

    def ReorderOddEven(self, pData):
        length = len(pData)
        return self.Reorder(pData, length, func=self.isNegtive)


S = Solution()
# print(S.reOrderArray3([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]))
# print(S.ReorderOddEven([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]))
print(S.ReorderOddEven([-1, 2, -3, 4, -5, -6, 7, 8, 9, 10, -10]))