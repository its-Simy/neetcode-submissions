class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0

        for n in range(len(prices)):
            for t in range(n,len(prices)):
                if prices[t]-prices[n] > res:
                    res = prices[t] - prices[n]
                
                
        return res
        
        