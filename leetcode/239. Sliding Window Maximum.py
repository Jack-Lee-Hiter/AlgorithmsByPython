'''
Given an array nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

For example,
Given nums = [1,3,-1,-3,5,3,6,7], and k = 3.

Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
Therefore, return the max sliding window as [3,3,5,5,6,7].
'''
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        if not nums or k <= 0:
            return []
        '''
        if you want to modify time complexity, you can write below:
        from collections import deque
        res, queue = [], deque()
        and replace queue.pop(0) with queue.popleft()
        '''
        res, queue = [], []
        for ind, val in enumerate(nums):
            if queue and queue[0] <= ind - k:
                queue.pop(0)
            while queue and nums[queue[-1]] < val:
                queue.pop()
            queue.append(ind)
            if ind + 1 >= k:
                res.append(nums[queue[0]])
        return res

s = Solution()
print(s.maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3))