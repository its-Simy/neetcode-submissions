class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #easiest but slow solution would be to do it in a double for loop approach

        '''
        list = 1,2,4,6
        prefix = [1,2,8,48]
        postfix = [48,48,24,6]

        '''
        n = len(nums)
        answer = [1] * n

        pre = 1
        for i in range(n):
            answer[i] = pre
            pre *= nums[i]
        post = 1
        for i in range(n-1,-1,-1):#backtracks this array so end to beginning (start,end, by what)
            answer[i] *= post
            post *= nums[i]

        return answer




        

