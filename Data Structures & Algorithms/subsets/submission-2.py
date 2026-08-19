class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        '''
        we think about this in a way where, we want to have a stack because we will do dfs, this wikl he like our our outlet, so we will add one item, call dfs with that new stack item, pop it, then call dfs on that, when we dint see anytbing else we append the item on therez


        we will have res as a self.res item to keep track od the list of lists. we will also have an index item in the dfs, , tbis will dictate where we are for the list provided
        '''

        self.res = []

        def dfs(stack, i):
            if i>= len(nums):
                print(stack)
                self.res.append(stack.copy())
                return
            stack.append(nums[i])
            dfs(stack, i+1)
            stack.pop()
            dfs(stack, i+1)
        dfs([],0)
        return self.res