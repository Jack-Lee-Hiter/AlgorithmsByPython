'''
在8*8的国际象棋上摆放八个皇后, 使其不能相互攻击, 即任意两个皇后不得处在同一行, 同一列或者同一对角线上
'''

'''
可以用回溯法, 也可以用下面的判别方法:
由于8各皇后的任意两个不能处在同一行, 那么肯定每一个皇后占据一行。
定义一个数组columnIndex[8], 数组中的第i个数字表示位于第i行的皇后列号
先把数组columnIndex[8]的8个数字分别用0-7初始化, 接下来就是对数组columnIndex的全排列
因为我们使用不同的数字初始化数组,所以任意两个皇后肯定不同列, 只需判断每一个排列对应的8个皇后是不是在一个对角线上
也就是对于下标i和j, 是不是abs(i-j) = columnIndex[i]-columnIndex[j]
'''

class Solution:
    # 全排列出所有顶点组合
    def Permutation(self, pointArr):
        if not len(pointArr):
            return []
        if len(pointArr) == 1:
            return pointArr
        numList = pointArr
        numList.sort()
        pStr = []
        for i in range(len(numList)):
            if i > 0 and numList[i] == numList[i-1]:
                continue
            temp = self.Permutation(numList[:i] + numList[i+1:])
            if type(temp[0]) == int:
                for j in temp:
                    pStr.append([numList[i]] + [j])
            else:
                for j in temp:
                    tempArr = [numList[i]] + j
                    pStr.append(tempArr)
        return pStr

    def Judge(self, alist):
        length = len(alist)
        for i in range(length):
            for j in range(length):
                if i == j:
                    continue
                if i - j == alist[i] - alist[j] or j - i == alist[i] - alist[j]:
                    return False
        return True

    def queen(self, alist):
        allAns = self.Permutation(alist)
        for tempList in allAns:
            isQueen = self.Judge(tempList)
            if isQueen:
                print(tempList)


s = Solution()
s.queen([0, 1, 2, 3, 4, 5, 6, 7])