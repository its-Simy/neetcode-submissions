class Solution:
    def permute(self, nums):

        self.res= []

        def backtrack(perms,idx):
            if idx == len(perms):
                self.res.append(perms[:])
                return
            for i in range(idx, len(perms)):
                perms[idx], perms[i] = perms[i],perms[idx]
                backtrack(perms,idx + 1)
                perms[idx],perms[i] = perms[i],perms[idx]
        
        backtrack(nums,0)
        return self.res
