class Solution:
    def maxArea(self, heights: List[int]) -> int:

        '''

        We have to return the max amout of water in the container

        each item in the list is how much water can be stored

        we know that whatever is the minimum bar we chose, we multiply 
        the difference plus 1 of right most bar - left most bar * least of the 2 bars
        ((right most - left most) + 1) * Least of two pointers
        ^ if we use normal count, not indicies

        brute force, two for loop approach, with the same math involved ^^^^
        
        5-0 = 5 * 1 = 5


        '''

        res = 0

        for left in range(len(heights)):
            for right in range(len(heights)-1,-1,-1):
                if right <= left:
                    break
                least =  heights[left] if heights[left] <= heights[right] else heights[right]
                amount = (right - left) * least
                if amount > res:
                    res = amount
        
        return res

    

    

        