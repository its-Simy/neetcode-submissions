class Solution:
    def maxArea(self, heights: List[int]) -> int:

        '''

            1 -> 7
            height: smallest of the two bars
            width:  biggest - smallest

            keep track of biggest area

            two pointers keeping track of the bars

            iterate only the smallest bar

            height: 2
            width 2-0 = 2
            area = 4
        '''
        
        res = 0
        l,r=0,len(heights)-1

        while l < r:

            #calculate
            area =  min(heights[l],heights[r])*(r-l)
            #compare
            res = max(res,area)
            #how to iterate
            if heights[l] <= heights[r]:
                l += 1  
            else:
                r -= 1


        return res

    

    

        