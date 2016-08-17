'''
Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note: The solution set must not contain duplicate triplets.

For example, given array S = [-1, 0, 1, 2, -1, -4],

A solution set is:
[[-1, 0, 1],[-1, -1, 2]]
'''

class Solution(object):
    def threeSum(self, nums):
        if nums == None or len(nums) < 3:
            return []
        elif len(nums) == 3 and sum(nums) == 0:
            return [sorted(nums)]

        nums.sort()                                 # sorted, O(nlogn)
        result, length = [], len(nums)
        for i in range(length - 2):
            if i > 0 and nums[i-1] == nums[i]:
                continue
            l, r = i + 1, length - 1                # i < l < r
            while l < r:
                Sum = nums[i] + nums[l] + nums[r]
                if Sum == 0:
                    result.append([nums[i], nums[l], nums[r]])
                    while l < r and nums[l] == nums[l + 1]:     # if appear same integer, l move right 1 place
                        l += 1
                    while l < r and nums[r] == nums[r - 1]:     # if appear same integer, r move left 1 place
                        r -= 1
                if Sum > 0:
                    r -= 1
                else:
                    l += 1
        return result
s = Solution()
print(s.threeSum([0, 0, 0, 0, 0]))