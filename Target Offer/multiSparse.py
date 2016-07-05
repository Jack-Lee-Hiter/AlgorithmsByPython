'''
利用三元组完成稀疏矩阵相乘
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

def multiTriple(tripleA, tripleB):
    rowA = shape(tripleA)[0]
    rowB = shape(tripleB)[0]
    multiMatrix = []
    for i in range(rowA):
        for j in range(rowB):
            if tripleA[i][1] == tripleB[j][0]:
                multiMatrix.append([tripleA[i][0], tripleB[j][1], tripleA[i][2]*tripleB[j][2]])
    return multiMatrix

def tripleToSparse(triple, m, n):
    outMatrix = zeros([m, n])
    for pointTuple in triple:
        mLocation = pointTuple[0]
        nLocation = pointTuple[1]
        value = pointTuple[2]
        outMatrix[mLocation][nLocation] = value
    return outMatrix

def matrixMultiple(matrixA, matrixB):
    mA, nA = shape(matrixA)
    mB, nB = shape(matrixB)
    if nA != mB:
        print("the two matries doesn't match!")
        return -1

    tripleA = sparseToTriple(matrixA)
    tripleB = sparseToTriple(matrixB)
    multiTriples = multiTriple(tripleA, tripleB)
    print(multiTriples)
    multiMatrix = tripleToSparse(multiTriples, mA, nB)
    return multiMatrix

matrixA = [[3, 0, 0, 7],
           [0, 0, -1, 0],
           [-1, -2, 0, 0],
           [0, 0, 0, 2]]
matrixB = [[0, 0, -2, 0, -1],
           [0, 0, -3, 0, 0],
           [-1, 0, 0, 0, 0],
           [0, 0, 0, 3, 0]]
ans = matrixMultiple(matrixA, matrixB)
print(ans)