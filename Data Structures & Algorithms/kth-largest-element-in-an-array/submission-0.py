class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        '''
        we are going to heap max the list, then pop k amount of times and the last pop would be the answer we return
        '''

        nums = [-s for s in nums]

        heapq.heapify(nums)

        for i in range(k):
            check = -(heapq.heappop(nums))
            if i == k-1:
                return check
