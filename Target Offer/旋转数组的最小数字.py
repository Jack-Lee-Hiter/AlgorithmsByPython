'''
把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。
输入一个递增排序的数组的一个旋转，输出旋转数组的最小元素。
例如数组{3,4,5,1,2}为{1,2,3,4,5}的一个旋转，该数组的最小值为1。
NOTE：给出的所有元素都大于0，若数组大小为0，请返回0。
'''

# -*- coding:utf-8 -*-
class Solution:
    def minNumber(self, Array):
        if len(Array) == 0:   # 如果数组为空，返回0
            return 0
        front = 0
        rear = len(Array) - 1
        
        if Array[rear] > Array[front]:    # 如果数组最后一个元素大于第一个元素，证明这个数组是不翻转的数组，直接返回第一个元素
            return Array[front]
        
        while (rear - front) > 1:
            mid = (front + rear) // 2   # 二分法比较数组中间元素，之所以想到二分法是因为数组是有序的
            if Array[mid] < Array[rear]:
                rear = mid
            if Array[front] < Array[mid]:
                front = mid
                
            if Array[front] == Array[mid] == Array[rear]:  # 对数特殊情况数组的判断，即当首中尾元素都相同的时候，二分法失效，只能顺序查找
                mid = 0
                for i in range(1, len(Array)):
                    if Array[mid] < Array[i]:
                        continue
                    else:
                        mid = i
                        
                return Array[mid]
                
        return Array[mid]

        
a = Solution()
Array = [3, 4, 5, 1, 2]
Array2 = [1, 2, 3, 4, 5]
Array3 = [1, 0, 1, 1, 1]
print(a.minNumber(Array))
print(a.minNumber(Array2))
print(a.minNumber(Array3))


    # 书上方法
    def minNumberInRotateArray2(self, rotateArray):
        if len(rotateArray) == 0:
            return 0
        front, rear = 0, len(rotateArray) - 1
        midIndex = 0
        while rotateArray[front] >= rotateArray[rear]:
            if rear - front == 1:
                midIndex = rear
                break
            midIndex = (front + rear) // 2
            if rotateArray[front] == rotateArray[rear] and rotateArray[front] == rotateArray[midIndex]:
                return self.MinInOrder(rotateArray, front, rear)

            if rotateArray[midIndex] >= rotateArray[front]:
                front = midIndex
            elif rotateArray[midIndex] <= rotateArray[rear]:
                rear = midIndex
        return rotateArray[midIndex]
    def MinInOrder(self, array, front, end):
        result = array[0]
        for i in array[front:end+1]:
            if i < result:
                result = i
        return result

Test = Solution()
print(Test.minNumberInRotateArray([3, 4, 5, 1, 2]))
print(Test.minNumberInRotateArray([1, 2, 3, 4, 5]))
print(Test.minNumberInRotateArray([1, 1, 1, 0, 1]))
print(Test.minNumberInRotateArray([1, 0, 1, 1, 1]))
print(Test.minNumberInRotateArray([]))
print(Test.minNumberInRotateArray([1]))