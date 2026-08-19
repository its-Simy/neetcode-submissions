class Solution:
    def combinationSum(self, nums, target):

        self.res = []

        def dfs(curAmount, pointer, stack):
            if curAmount > target:
                return

            if curAmount == target:
                
                self.res.append(stack.copy())
                return

            if pointer >= len(nums):
                return
            
            stack.append(nums[pointer])
            dfs(curAmount + nums[pointer], pointer,stack)
            stack.pop()
            dfs(curAmount, pointer+1,stack)
        dfs(0,0,[])
        return self.res

            
            
