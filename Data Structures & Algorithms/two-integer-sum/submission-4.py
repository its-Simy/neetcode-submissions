class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
        we have to make sure that nums[i] and nums[j] equal the target

        so here i could have a dictionary

        the key would be the number in the list, the value would be the index

        so we would check if there is a item in the dictionary that has the difference between target - item. if it does then we return it in correct ordered from which would always be the item from the dictionary then the new item we found


        dic = {}

        loop through

        use the .get method for dictionaries, if its not in there set to false
        if not true
            append the item to the dictionary
        
        else
        return the values
        ''' 

        dic = {}

        for current in range(len(nums)):
            diff = target - nums[current]
            if not diff in dic:
                dic[nums[current]] = current
            else:
                val = dic[diff]
                return [val,current]
        return