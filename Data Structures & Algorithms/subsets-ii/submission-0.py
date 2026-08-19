class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        def sub(stack,pointer):      
            if pointer == len(nums):
                res.append(stack.copy())
                return

            stack.append(nums[pointer])
            sub(stack, pointer + 1)
            stack.pop()

            while pointer + 1 < len(nums) and nums[pointer] == nums[pointer+1]:
                pointer += 1
            sub(stack, pointer + 1)
            
        sub([],0)
        return res