class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
    
        if(len(s) != len(t)):
            return False


        #Building and filling hashmaps
        countS,countT = {},{}
        for i in range(len(s)):
            countS[s[i]] =  1 + countS.get(s[i],0)#if the key doesnt exist, then return 0
            countT[t[i]] =  1 + countT.get(t[i],0)


        #if the hashmaps numbers aren't alike, return false
        for x in countS:
            #use the .get because if there is not a certain char, it will default to 0
            if (countS[x] != countT.get(x,0)):
                return False
        

        return True