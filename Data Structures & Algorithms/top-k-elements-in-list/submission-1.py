class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if k == len(nums):
            return nums

        answer = []#list we will return, make it the size of k,
        dic = {}

        #sets counts
        for i in range(len(nums)):
            #checks if key is in hash, if not defaults to false
            #if true, adjust count
            if dic.get(nums[i],False):
                count = dic.get(nums[i],False) + 1
                dic[nums[i]] = count
            else:
                dic[nums[i]] = 1

        #completes k amount of times.
        for i in range(k):
            n = max(dic, key=dic.get)
            answer.append(n)#append
            del dic[n]


        return answer
        
        