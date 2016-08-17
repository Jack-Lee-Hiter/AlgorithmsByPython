'''
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution.
Given nums = [2, 7, 11, 15], target = 9,
Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
'''

class Solution():
    def twoSum(self, nums, target):
        hashdict = {}
        for i, item in enumerate(nums):
            if (target - item) in hashdict:
                return (hashdict[target - item], i)
            hashdict[item] = i
        return (-1, -1)
s = Solution()
print(s.twoSum([2, 7, 11, 15], 9))