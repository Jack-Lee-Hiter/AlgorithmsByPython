'''
稀疏矩阵的转置
输入: 一个稀疏矩阵
输出: 矩阵的转置
方法: 中间可以利用三元组进行操作
'''
from numpy import *
def sparseToTriple(matrix):
    m, n = shape(matrix)
    triple = []
    for i in range(m):
        for j in range(n):
            if matrix[i][j] != 0:
                triple.append([i, j, matrix[i][j]])
    return triple

def transTriple(triple):
    m, n = shape(triple)
    transMatrix = []
    sortedIndex = array([m[1] for m in triple]).argsort()
    for i in range(m):
        tempArray = triple[sortedIndex[i]]
        transMatrix.append([tempArray[1], tempArray[0], tempArray[2]])
    return transMatrix

def tripleToSparse(triple, m, n):
    outMatrix = zeros([n, m])
    for pointTuple in triple:
        mLocation = pointTuple[0]
        nLocation = pointTuple[1]
        value = pointTuple[2]
        outMatrix[mLocation][nLocation] = value
    return outMatrix

def matrixTrans(matrix):
    m, n = shape(matrix)
    triple = sparseToTriple(matrix)
    transedTriple = transTriple(triple)
    transedMatrix = tripleToSparse(transedTriple, m, n)
    return transedMatrix

matrix = [[0, 0, 0, 0, 0, 0, 6, 0, 0],
          [0, 0, 2, 0, 0, 1, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0],
          [3, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 5, 0],
          [0, 7, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 8],
          [0, 0, 5, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 2, 0, 0, 0, 0, 0]]

transedMatrix = matrixTrans(matrix)
print(transedMatrix)