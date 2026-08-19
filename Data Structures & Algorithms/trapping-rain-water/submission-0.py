class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        l,r = 0,len(height)-1
        leftMAX,rightMAX = height[l],height[r]

        while r > l:
            if leftMAX < rightMAX:
                l += 1
                leftMAX = max(leftMAX,height[l])
                res += leftMAX - height[l]
            else:
                r -= 1
                rightMAX = max(rightMAX,height[r])
                res += rightMAX - height[r]
        
        return res
                
            

