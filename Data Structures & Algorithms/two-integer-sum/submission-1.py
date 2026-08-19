class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #never going to be less that 2 items in the list
        #numbers and target can be negative
        #there is always and answer
        #brute force answer: double loop O(n^2)
        '''
        faster solution could be with a hashmap: fast get time(O(1))
        '''
        answer = [] #list that has to be returned
        dic = {} #hashmap



        #first create hashmap
        for i, n in enumerate(nums):
            #does i = normal index, then n = values nums[i]
            difference = target - n
            if(dic.get(difference) != None):
                answer.append(dic[difference])
                answer.append(i)
            
            dic[n] = i
    
        return answer

        
        
