from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countOfVals = Counter(nums)
        vals = sorted(countOfVals, key=countOfVals.get, reverse=True)
        res = []
        c = 0
        for i in vals:
            if(c == k):
                break
            res.append(i)
            c += 1
        return res

