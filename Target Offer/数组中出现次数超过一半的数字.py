'''
数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。
例如输入一个长度为9的数组{1,2,3,2,2,2,5,4,2}。由于数字2在数组中出现了5次，超过数组长度的一半，因此输出2。如果不存在则输出0。
'''

# -*- coding:utf-8 -*-
class Solution:
    # 基于Partition函数的O(n)算法
    def MoreThanHalfNum_Solution(self, numbers):
        length = len(numbers)
        if length == 1:
            return numbers[0]
        if self.CheckInvalidArray(numbers, length):
            return 0

        middle = length >> 1
        start = 0
        end = length - 1
        index = self.Partition(numbers, length, start, end)
        while index != middle:
            if index > middle:
                end = index - 1
                index = self.Partition(numbers, length, start, end)
            else:
                start = index + 1
                index = self.Partition(numbers, length, start, end)
        result = numbers[middle]
        if not self.CheckMoreThanHalf(numbers, length, result):
            result = 0
        return result
    # 划分算法
    def Partition(self, numbers, length, start, end):
        if numbers == None or length <= 0 or start < 0 or end >= length:
            return None
        if end == start:
            return end
        pivotvlue = numbers[start]
        leftmark = start + 1
        rightmark = end

        done = False

        while not done:
            while numbers[leftmark] <= pivotvlue and leftmark <= rightmark:
                leftmark += 1
            while numbers[rightmark] >= pivotvlue and rightmark >= leftmark:
                rightmark -= 1

            if leftmark > rightmark:
                done = True
            else:
                numbers[leftmark], numbers[rightmark] = numbers[rightmark], numbers[leftmark]
        numbers[rightmark], numbers[start] = numbers[start], numbers[rightmark]
        return rightmark

    # 检查输入的数组是否合法
    def CheckInvalidArray(self, numbers, length):
        InputInvalid = False
        if numbers == None or length <= 0:
            InputInvalid = True
        return InputInvalid
    # 检查查找到中位数的元素出现次数是否超过所有元素数量的一半
    def CheckMoreThanHalf(self, numbers, length, number):
        times = 0
        for i in range(length):
            if numbers[i] == number:
                times += 1
        if times*2 <= length:
            return False
        return True
#-------------------------------以上都是基于划分的方法寻找---------------------------------#
    # 根据数组特点找出O(n)的算法
    def MoreThanHalfNum(self, numbers):
        length = len(numbers)
        if numbers == None or length <= 0:
            return 0
        result = numbers[0]
        times = 1
        for i in range(1, length):
            if times == 0:
                result = numbers[i]
                times = 1
            elif numbers[i] == result:
                times += 1
            else:
                times -= 1
        if not self.CheckMoreThanHalf(numbers, length, result):
            result = 0
        return result

S = Solution()
# print(S.MoreThanHalfNum_Solution([1, 2, 3, 2, 2, 2, 5, 4, 2]))
# print(S.MoreThanHalfNum_Solution([1, 2, 3, 3, 3, 3, 4]))
# print(S.MoreThanHalfNum_Solution([1, 2]))
print(S.MoreThanHalfNum([1, 2, 3, 2, 2, 2, 5, 4, 2]))
print(S.MoreThanHalfNum([1, 2, 3, 3, 3, 3, 4]))
print(S.MoreThanHalfNum([1, 2]))