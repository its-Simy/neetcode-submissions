class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = strs[0]
        size = len(res)

        for word in strs[1:]:
            
            while res != word[0:size]:
                size -= 1
                res = res[0:size]
                if size == 0:
                    return ""
        return res


