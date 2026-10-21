class Solution:
    def twoSum(self, nums, target):
        dic = {}
        for current in range(len(nums)):
            diff = target - nums[current]
            if not diff in dic:
                dic[nums[current]] = current
            else:
                return [dic[diff],current]
        return