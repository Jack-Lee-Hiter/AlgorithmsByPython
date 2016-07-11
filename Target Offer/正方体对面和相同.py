'''
输入一个含有八个数字的数组, 判断有没有可能把这把个数字分别放到正方体的八个顶点上
使得正方体上三组相对的面上四个顶点的和都相等
'''

'''
这个问题其实就是字符串排列的一个衍生问题
输入一个数组, 生成这八个数字所有可能的排列, 对应到正方体的八个顶点上
检查是否满足题目要求即可
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
    def compareSum(self, alist):
        allAns = self.Permutation(alist)
        for tempList in allAns:
            sum1 = tempList[0] + tempList[1] + tempList[2] + tempList[3]
            sum2 = tempList[4] + tempList[5] + tempList[6] + tempList[7]
            sum3 = tempList[0] + tempList[2] + tempList[4] + tempList[6]
            sum4 = tempList[1] + tempList[3] + tempList[5] + tempList[7]
            sum5 = tempList[0] + tempList[1] + tempList[4] + tempList[5]
            sum6 = tempList[2] + tempList[3] + tempList[6] + tempList[7]
            if sum1 == sum2 and sum3 == sum4 and sum5 == sum6:
                return True
        return False
ss = [2, 3, 9, 7, 0, 11, 2, 6]
ss2 = [1, 1, 1, 1, 1, 1, 1, 1]
s = Solution()
print(s.compareSum(ss2))