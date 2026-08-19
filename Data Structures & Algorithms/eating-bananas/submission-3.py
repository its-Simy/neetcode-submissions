class Solution:
    def minEatingSpeed(self, piles, h):
        res = max(piles)
        l,r = 1, max(piles)
        while l <= r:
            mid = (l+r) // 2
            totalTime = 0
            for i in piles:
                totalTime += math.ceil(float(i) / mid)
            if totalTime <= h:
                res = mid
                r = mid - 1
            else:
                l = mid + 1;
        
        return res
            