class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #easiest but slow solution would be to do it in a double for loop approach

        #2 things to consider
            #0's in the problem
            #product of all the elements of nums except nums[i]
        
        answer = [0] * len(nums)
        a = 1
        negative = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                a *= nums[i]
            else:
                negative += 1
    
        for i in range(len(nums)):
            if nums[i] != 0 and negative == 0:
                answer[i] = int(a / nums[i])
            elif nums[i] == 0 and negative == 1:
                answer[i] = a
            else:
                answer[i] = 0

        return answer        
        

