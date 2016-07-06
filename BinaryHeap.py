# 构建树实现堆
class BinHeap:
    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0

    #插入新结点后必要时交换子节点和父节点的位置保持堆的性质
    def percUp(self, i):
        while i//2 > 0:
            if self.heapList[i] < self.heapList[i//2]:
                temp = self.heapList[i//2]
                self.heapList[i//2] = self.heapList[i]
                self.heapList[i] = temp
            i = i//2

    # 插入节点
    def insert(self, k):
        self.heapList.append(k)
        self.currentSize += 1
        self.percUp(self.currentSize)

    # 删除堆顶元素后, 交换堆尾和空堆顶的位置并实现元素的下沉
    def percDown(self, i):
        while (i*2) <= self.currentSize:
            mc = self.minChild(i)
            if self.heapList[i] > self.heapList[mc]:
                temp = self.heapList[i]
                self.heapList[i] = self.heapList[mc]
                self.heapList[mc] = temp
            i = mc

    def minChild(self, i):
        if i * 2 + 1 > self.currentSize:
            return i * 2
        else:
            if self.heapList[i*2] < self.heapList[i*2+1]:
                return i * 2
            else:
                return i * 2 + 1

    def delMin(self):
        retval = self.heapList[1]
        self.heapList[1] = self.heapList[self.currentSize]
        self.currentSize = self.currentSize - 1
        self.heapList.pop()
        self.percDown(1)
        return retval

    def buildHeap(self, alist):
        i = len(alist) // 2
        self.currentSize = len(alist)
        self.heapList = [0] + alist[:]
        while (i > 0):
            self.percDown(i)
            i = i - 1
        return self.heapList

H = BinHeap()
print(H.buildHeap([9, 6, 5, 2, 3]))