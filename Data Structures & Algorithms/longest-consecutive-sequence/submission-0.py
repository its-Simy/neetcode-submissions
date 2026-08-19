class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #First understand what their asking
        #has to go up by exactly one, and then the return is the none in order amount.


        #What are the possible limitations
        # what if theres 2 different sequences, how do i know how to keep track of which to do


        #Possible methods
        


        #edge cases
        #what if theres nothing.
        #simply repeating elements        


        answer = 0

        nums.sort()
        for n in range(len(nums)):
            track = nums[n]
            conseq = 1
            for q in nums:
                if q == (track + 1):
                    track += 1
                    conseq += 1
            if conseq > answer:
                answer = conseq   

        return answer