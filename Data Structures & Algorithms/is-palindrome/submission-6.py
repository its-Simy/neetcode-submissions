class Solution:
    def isPalindrome(self, s: str) -> bool:
        '''
            this is case insensitive so we just have to go from the front
            and from the back, check if its the same letter

            if its not alphanumberic just skip
        '''

        l,r = 0,len(s)-1

        while (l < r):
            while l < r and not s[l].isalnum():
                l += 1
            while l < r and not s[r].isalnum():
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        
        return True


