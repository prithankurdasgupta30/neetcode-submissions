class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        i=0
        j=len(height)-1
        left=height[i]
        right=height[j]
        res = 0
        while i<j:
            if left < right:
                i+=1
                left = max(left,height[i])
                res += left - height[i]
            else:
                j-=1
                right = max(right,height[j])
                res += right - height[j]
        return res