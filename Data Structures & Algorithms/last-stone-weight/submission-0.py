class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        '''
            retrieve the 2 heaviest stones
                max heap would be needed for this

                
            with the two results check th other conditions
        ''' 
        heapq.heapify_max(stones)
        res = 0

        while len(stones) >= 2:
            x,y = heapq.heappop_max(stones),heapq.heappop_max(stones)

            if x < y:
                heapq.heappush_max(stones, y-x)
            elif y < x:
                heapq.heappush_max(stones, x-y)
        
        return 0 if len(stones) == 0 else heapq.heappop_max(stones)

            

            


