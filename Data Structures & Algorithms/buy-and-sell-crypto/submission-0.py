class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        minS = prices[0]
        for sell in prices:
            maxP = max(maxP, sell-minS)
            minS = min(minS, sell)
        return maxP
        