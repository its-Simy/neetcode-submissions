class Solution:
    def combinationSum2(self, nums, target):
        self.res = []
        nums.sort()

        def dfs(total,pointer, stack):
            if total == target:
                self.res.append(stack.copy())
                return
            if pointer >= len(nums) or total > target:
                return
            
            stack.append(nums[pointer])
            dfs(total + nums[pointer], pointer + 1, stack)
            stack.pop()
            while pointer + 1 < len(nums) and nums[pointer] == nums[pointer+1]:
                pointer += 1

            dfs(total, pointer + 1, stack)
        
        dfs(0,0,[])
        return self.res