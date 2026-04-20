class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged = nums1 + nums2
        merged.sort()
        totalLen = len(merged)
        if totalLen%2 == 0:
            x = (merged[totalLen//2 -1] + merged[totalLen//2])/2
            return x
        else:
            x = merged[totalLen//2]
            return x