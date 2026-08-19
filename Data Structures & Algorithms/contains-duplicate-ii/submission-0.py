class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        '''
            Work through
            2 == 2
            |0-2| = 2
            2 <= K (K == 1)

            |0 - 3| = 3
            3 <= 3

            ---------------------------------------------------------
            Edge Cases:

            when length is 1

            -----------------------------------------------------------

            Approach 1:

            make a dictionary
            keys the actual number, indicy be the value pair

            TC O(n)
            SC O(n)

            -------------------------------------------------------------

            Approach 2:

            brute force, nested for loop
            TC O(n^2)
            SC O(1)
        '''

        for left in range(len(nums)):
            for right in range(left + 1,len(nums)):
                if nums[left] == nums[right] and abs(left - right) <= k:
                    return True 



        return False


        