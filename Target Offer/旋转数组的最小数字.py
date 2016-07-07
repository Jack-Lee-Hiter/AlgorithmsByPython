'''
把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。
输入一个递增排序的数组的一个旋转，输出旋转数组的最小元素。
例如数组{3,4,5,1,2}为{1,2,3,4,5}的一个旋转，该数组的最小值为1。
NOTE：给出的所有元素都大于0，若数组大小为0，请返回0。
'''

# -*- coding:utf-8 -*-
class Solution:
    def minNumberInRotateArray(self, rotateArray):
        if len(rotateArray) == 0:
            return 0
        front = 0
        rear = len(rotateArray) - 1
        minVal = rotateArray[0]
        if rotateArray[front] < rotateArray[rear]:
            return rotateArray[front]
        else:
            while (rear - front) > 1:
                mid = (rear + front)//2
                if rotateArray[mid] > rotateArray[rear]:
                    front = mid
                elif rotateArray[mid] < rotateArray[front]:
                    rear = mid
                elif rotateArray[mid] == rotateArray[front] and rotateArray[front] == rotateArray[rear]:
                    for i in range(1, len(rotateArray)):
                        if rotateArray[i] < minVal:
                            minVal = rotateArray[i]
                            rear = i
            minVal = rotateArray[rear]
            return minVal

Test = Solution()
print(Test.minNumberInRotateArray([3, 4, 5, 1, 2]))
print(Test.minNumberInRotateArray([1, 2, 3, 4, 5]))
print(Test.minNumberInRotateArray([1, 1, 1, 0, 1]))
print(Test.minNumberInRotateArray([1, 0, 1, 1, 1]))
print(Test.minNumberInRotateArray([]))
print(Test.minNumberInRotateArray([1]))