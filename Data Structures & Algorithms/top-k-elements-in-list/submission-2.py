from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''
        we need to return back the k most frequent numbers

        - the naieve way to do this is to use counter on this
        - sort
        loop to build res list
        return res

        O(n) time complexity and O(n + k) space complexity
        n for the dictionary and k for the returned answer
        '''
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

