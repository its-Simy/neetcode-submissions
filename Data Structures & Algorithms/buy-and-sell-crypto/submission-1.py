class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        minVal = prices[0]

        for time in prices:
            maxP = max(maxP, time - minVal)
            minVal = min (minVal, time)
        return maxP
        
        