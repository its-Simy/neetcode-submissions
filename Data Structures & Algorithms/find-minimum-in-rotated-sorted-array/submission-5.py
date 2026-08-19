class Solution:
    def findMin(self, n):
        l,r = 0,len(n)-1
        res = n[0]
        while l <= r:
            if n[l] < n[r]:
                res = min(res,n[l])
            mid = (l+r) // 2
            res = min(res,n[mid])
            if n[mid] >= n[l]:
                l = mid + 1
            else:
                r = mid - 1

        return res
