class Solution:
    def letterCombinations(self, d):
        combos = {"2": ["a","b","c"],"3": ["d","e","f"],"4": ["g","h","i"],"5": ["j","k","l"],"6": ["m","n","o"],"7": ["p","q","r","s"],"8": ["t","u","v"],"9": ["w","x","y","z"]}    
        res = []
        def backtrack(i,curStr):
            if len(curStr) == len(d):
                res.append(curStr)
                return
            for c in combos[d[i]]:
                backtrack(i+1,curStr + c)
        if d:
            backtrack(0,"")
        return res