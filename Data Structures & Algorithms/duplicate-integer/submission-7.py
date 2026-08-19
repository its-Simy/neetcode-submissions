class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if (len(nums) < 1):
            return False 

        checker = set()
        for i in nums:
            checker.add(i)
        
        if(len(checker) < len(nums)):
            return True

        return False