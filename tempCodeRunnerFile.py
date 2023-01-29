class Solution:
    def twoSum(nums, target):
        for i, j in enumerate(nums):
            out = target - j
            if out in nums:
                return [i, nums.index(out)]
            break