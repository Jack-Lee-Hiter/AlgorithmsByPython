'''
输入n个整数，找出其中最小的K个数。例如输入4,5,1,6,2,7,3,8这8个数字，则最小的4个数字是1,2,3,4。
'''

class Solution:
    # O(n)的算法, 只有当我们可以修改输入的数组时可用
    # 基于Partition的方法
    def GetLeastNumbers_Solution(self, tinput, k):
        if tinput == None or len(tinput) < k or len(tinput) <= 0 or k <=0:
            return []
        n = len(tinput)
        start = 0
        end = n - 1
        index = self.Partition(tinput, n, start, end)
        while index != k-1:
            if index > k-1:
                end = index - 1
                index = self.Partition(tinput, n, start, end)
            else:
                start = index + 1
                index = self.Partition(tinput, n, start, end)
        output = tinput[:k]
        output.sort()
        return output

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
    # O(nlogk)的算法, 适合海量数据
    # 利用一个k容量的容器存放数组, 构造最大堆, 当下一个数据大于最大数, 跳过, 小于最大数, 则进入容器替换之前的最大数
    def GetLeastNumbers(self, tinput, k):
        import heapq
        if tinput == None or len(tinput) < k or len(tinput) <= 0 or k <= 0:
            return []
        output = []
        for number in tinput:
            if len(output) < k:
                output.append(number)
            else:
                # 构造最小堆， 不推荐
                # output = heapq.nsmallest(k, output)
                # if number >= output[-1]:
                #     continue
                # else:
                #     output[-1] = number
                # 构造最大堆， 推荐
                output = heapq.nlargest(k, output)
                if number >= output[0]:
                    continue
                else:
                    output[0] = number
        return output[::-1]     # 最小堆用 return output
tinput = [4,5,1,6,2,7,3,8]
s = Solution()
print(s.GetLeastNumbers_Solution(tinput, 4))
print(s.GetLeastNumbers(tinput, 4))
print(s.GetLeastNumbers(tinput, 5))
