class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #easiest but slow solution would be to do it in a double for loop approach

        #2 things to consider
            #0's in the problem
            #product of all the elements of nums except nums[i]
        
        answer = [0] * len(nums)

        for i in range(len(nums)):
            point = 1
            for j in range(len(nums)):
                if j == i:
                    ++j
                else:
                    point *= nums[j]
                
            answer[i] = point

        return answer        
        

