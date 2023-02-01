class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        r = nums1+nums2
        r.sort()
        rl = len(r)
        return r[rl//2] if rl % 2 == 1 else (r[rl//2 - 1] + r[rl//2])/2