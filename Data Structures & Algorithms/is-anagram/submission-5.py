from collections import Counter
class Solution:
    def isAnagram(self, s, t):
        if len(s) != len(t) or Counter(s) != Counter(t):
            return False
        
        return True

        
        