class Solution:
    def isPalindrome(self, s: str) -> bool:
        #not case sensitive
        #ignores non-alphanumeric characters

        #start from beginning and also the end
        #if the beginning or the end aren't Alphanumeric, skip THEN perform check

        #isalnum(), will check for alphanumeric
        if len(s) == 1:
            return True

        j = len(s)-1
        start = 0

        for i in range(len(s)):
        #check for alphanumeric
            while (start < len(s) and s[start].isalnum() != True):
                start = start+1
            while (s[j].isalnum() != True and j > -1):
                j = j-1
             # if they equal eachother(odd length) or i surpasses j then return true
            if(start > len(s) or j < 0 or start == j or start > j):
                return True
        #are they equal to eachother?, if not return false
            if(s[start].upper() != s[j].upper()):
                return False
       
            j-=1
            start+=1


        return True



