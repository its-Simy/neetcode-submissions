class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 1:
            return [strs]
        
        tracker = {}
        res = []

        for word in strs:
            check = sorted(word)
            check = "".join(check)
            if check in tracker:
                tracker[check].append(word)
            else:
                tracker[check] = [word]
        
        for listItems in tracker.values():
            res.append(listItems)
        
        return res
