# -*- coding:utf-8 -*-
'''
Given an unsorted array of integers, find the length of longest increasing subsequence.

For example,
Given [10, 9, 2, 5, 3, 7, 101, 18],
The longest increasing subsequence is [2, 3, 7, 101], therefore the length is 4. Note that there may be more than one LIS combination, it is only necessary for you to return the length.

Your algorithm should run in O(n^2) complexity.

Follow up: Could you improve it to O(n log n) time complexity?
'''


class Solution(object):
    # 原始O(nlogn)方法
    def lengthOfLIS(self, nums):
        tails = [0] * len(nums)
        size = 0
        for x in nums:
            i, j = 0, size
            while i != j:
                mid = (i + j) // 2
                if tails[mid] < x:
                    i = mid + 1
                else:
                    j = mid
            tails[i] = x
            size = max(i + 1, size)
        return size
    # 简单优化的O(nlogn)方法, 1000000长度为8的数据平均节约0.5s
    def lengthOfLIS2(self, nums):
        tails = [0] * len(nums)
        size = 0
        for x in nums:
            i, j = 0, size
            if j > 0 and tails[j - 1] < x:
                tails[j] = x
                size += 1
                continue
            while i != j:
                mid = (i + j) // 2
                if tails[mid] < x:
                    i = mid + 1
                else:
                    j = mid
            tails[i] = x
            size = max(i + 1, size)
        return size

s = Solution()
aList = [3, 2, 4, 9, 10, 22, 15, 17, 23, 6]
print(s.lengthOfLIS(aList), s.lengthOfLIS2(aList))