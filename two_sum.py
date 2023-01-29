# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
        
#         d = {}
#         for i, j in enumerate(nums):
#             r = target - j
#             if r in d: return [d[r], i]
#             d[j] = i


class Solution:
    def twoSum(nums, target):
        for i, j in enumerate(nums):
            out = target - j
            if out in nums:
                lt =  [i, nums.index(out)]
                break
        return lt

nums = [2,7,11,15]
target = 9
print(Solution.twoSum(nums, target))

