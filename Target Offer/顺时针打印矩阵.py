'''
输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字，
例如，如果输入如下矩阵：
[[ 1,  2,  3,  4],
 [ 5,  6,  7,  8],
 [ 9, 10, 11, 12],
 [13, 14, 15, 16]]
则依次打印出数字 1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10.
'''

# -*- coding:utf-8 -*-
class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        if matrix == None:
            return
        rows = len(matrix)
        columns = len(matrix[0])
        start = 0
        while rows > start * 2 and columns > start * 2:
            self.PrintMatrixInCircle(matrix, columns, rows, start)
            start += 1
        print('')

    def PrintMatrixInCircle(self, matrix, columns, rows, start):
        endX = columns - 1 - start
        endY = rows - 1 - start

        # 从左到右打印一行
        for i in range(start, endX+1):
            number = matrix[start][i]
            print(number, ' ', end='')

        # 从上到下打印一行
        if start < endY:
            for i in range(start+1, endY+1):
                number = matrix[i][endX]
                print(number, ' ', end='')

        # 从右到左打印一行
        if start < endX and start < endY:
            for i in range(endX-1, start-1, -1):
                number = matrix[endY][i]
                print(number, ' ', end='')

        # 从下到上打印一行
        if start < endX and start < endY-1:
            for i in range(endY-1, start, -1):
                number = matrix[i][start]
                print(number, ' ', end='')

    # 直接一个完整的函数实现这个功能
    def PrintMatrix(self, matrix):
        printArr = []
        if matrix == None:
            return
        if matrix == []:
            return []
        start = 0               # 每次循环时起始点
        rows = len(matrix)   # 列数
        columns = len(matrix[0])   # 行数

        while columns > 2 * start and rows > 2 * start:
            endX = columns - 1 - start
            endY = rows - 1 - start

            # 从左到右将数字存入printArr
            for i in range(start, endX+1):
                number = matrix[start][i]
                printArr.append(number)

            # 从上到下将数字存入printArr
            if start < endY:
                for i in range(start+1, endY+1):
                    number = matrix[i][endX]
                    printArr.append(number)

            # 从右到左将数字存入printArr
            if start < endX and start < endY:
                for i in range(endX-1, start-1, -1):
                    number = matrix[endY][i]
                    printArr.append(number)

            # 从下到上将数字存入printArr
            if start < endX and start < endY-1:
                for i in range(endY-1, start, -1):
                    number = matrix[i][start]
                    printArr.append(number)
            start += 1
        return printArr


matrix = [[1,  2,  3,  4],
          [5,  6,  7,  8],
          [9, 10, 11, 12],
          [13, 14, 15, 16]]
matrix2 = [[1],[2],[3],[4],[5]]
matrix3 = [[1,2],[3,4],[5,6],[7,8],[9,10]]
S = Solution()
S.printMatrix(matrix)
S.printMatrix(matrix2)
S.printMatrix(matrix3)
# print(S.PrintMatrix(matrix))
# print(S.PrintMatrix(matrix2))
# print(S.PrintMatrix(matrix3))