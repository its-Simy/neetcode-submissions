class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        my_dic={}
        #if there are no items or 1 item, return false
        if(len(nums) == 0 or len(nums) == 1):
            return False


        for i, items in enumerate(nums):
            my_dic[items] = i
    
        if(len(my_dic) != len(nums)):
            return True
        
        return False