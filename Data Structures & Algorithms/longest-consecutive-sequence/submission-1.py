class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        answer = 0
        numSet = set(nums)

        
        for n in numSet:
            tracker = 1
            current = n
            while n - 1 not in numSet:
                if current + 1 in numSet:
                    tracker += 1
                    current += 1
                else:
                    break

            if tracker > answer:
                answer = tracker

        return answer