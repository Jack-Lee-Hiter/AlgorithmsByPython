class nearestPoint:
    def __init__(self, aList):
        self.aList = aList

    def calculate(self):
        if self.aList == None or len(self.aList) == 0:
            return
        if len(self.aList) == 1:
            return 0

        global xRangeList, yRangeList
        xRangeList, yRangeList = self.Mergesort(self.aList, 0), self.Mergesort(self.aList, 1)
        return self.ClosestPair(xRangeList, yRangeList)

    def Mergesort(self, aList, axis):
        if len(aList) <= 1:
            return aList
        pivot = len(aList)//2
        leftArray = aList[:pivot]
        rightArray = aList[pivot:]
        return self.Merge(self.Mergesort(leftArray, axis), self.Mergesort(rightArray, axis), axis)
    def Merge(self, leftList, rightList, axis):
        output = []
        leftIndex, rightIndex = 0, 0
        while leftIndex < len(leftList) and rightIndex < len(rightList):
            if leftList[leftIndex][axis] < rightList[rightIndex][axis]:
                output.append(leftList[leftIndex])
                leftIndex += 1
            else:
                output.append(rightList[rightIndex])
                rightIndex += 1
        while leftIndex < len(leftList):
            output.append(leftList[leftIndex])
            leftIndex += 1
        while rightIndex < len(rightList):
            output.append(rightList[rightIndex])
            rightIndex += 1
        return output

    def ClosestPair(self, xList, yList):
        if len(xList) == 2:
            temp1 = ((xList[0][0]-xList[1][0])**2+(xList[0][1]-xList[1][1])**2)**0.5
            temp2 = ((yList[0][0]-yList[1][0])**2+(yList[0][1]-yList[1][1])**2)**0.5
            return min(temp1, temp2)
        elif len(xList) == 3:
            temp1 = min((xList[1][0] - xList[0][0])**2 + (xList[1][1] - xList[0][1])**2, (yList[1][0] - yList[0][0])**2 + (yList[1][1] - yList[0][1])**2)
            temp2 = min((xList[2][0] - xList[0][0])**2 + (xList[2][1] - xList[0][1])**2, (yList[2][0] - yList[0][0])**2 + (yList[2][1] - yList[0][1])**2)
            temp3 = min((xList[2][0] - xList[1][0])**2 + (xList[2][1] - xList[1][1])**2, (yList[2][0] - yList[1][0])**2 + (yList[2][1] - yList[1][1])**2)
            temp = min(temp1, temp2)
            return (min(temp, temp3))**0.5
        else:
            length = len(xList)
            pivot = length//2
            xLeft, xRight, yLeft, yRight = xList[:pivot], xList[pivot:], yList[:pivot], yList[pivot:]
            d1, d2 = self.ClosestPair(xLeft, yLeft), self.ClosestPair(xRight, yRight)
            d = min(d1, d2)

            m = xList[pivot][0]
            S = []
            for i in range(len(yList)):
                if abs(yList[i][0] - m) < d:
                    S.append(yList[i])
            dminsq = d**2
            if len(S) > 2:
                for i in range(len(S)-1):
                    k = i + 1
                    while k <= len(S) - 1 and (S[k][1] - S[i][1])**2 < dminsq:
                        dminsq = min((S[k][0]-S[i][0])**2+(S[k][1]-S[i][1])**2, dminsq)
                        k += 1
            elif len(S) == 2:
                dminsq = min((S[1][0]-S[0][0])**2+(S[1][1]-S[0][1])**2, dminsq)
        return dminsq**0.5



A = [[3.7,2.7],[6.9,10.2],[10.5,6.3],[2.0,5.2],[7.6,9.6],[6.4,6.8],[8.9,6.3],[4.8,9.9],[3.1,6.1],[5.3,5.8],[3.6,8.1],[2.9,3.7],[3.2,4.1],[4.7,3.9]]
s = nearestPoint(A)
print(s.calculate())
