class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        '''
            I can do k amout of replacements of characters with any other character in the string
            
            goal: make the longest substring with a repeating character

           we would make 2 pointers,

                make a dynamic window

                we would use a dictionary

                    fast lookups to compare total amout of items in the subset to the number of repitions of the current value

                    window: [a], hash: [a,1]: Total is 1
                    window: [a,a], hash: [a,2]: Total is 2
                    window: [a,a,a], hash: [a,3]: total is 3
                    window: [a,a,a,b], hash: [a,3] [b,1]: total would be 4 check valid if total - current <=k
                    window: [a,a,a,b,a], hash: [a,4] [b,1]: total is 5 (also checks but passes)
                    window: [a,a,a,b,a,b], hash: [a,4] [b,2]: total is 6 check if valid
                        left pointer increments because didn't pass
                    window: [a,a,b,a,b], hash: [a,3] [b,2]: total is 5, see that total - current > 1
                    window: [a,b,a,b], hash: [a,2] [b,2]: total is 5
        '''

        if len(s) == 1:
            return 1
        
        left = 0

        res = 0

        checker = {}

        #because if it surpases right, then the string has technically ended
        for right in range(len(s)):
            total = (right - left) + 1
            
            #This adds every part of the substring to the hashtable
            if checker.get(s[right],False):
                checker[s[right]] += 1
            else:
                checker[s[right]] = 1
            maxSub = max(checker.values())
            if total - maxSub <= k:
                right +=1
                res = max(res,total)
            else:
                checker[s[left]] -=1
                left += 1
                right -=1

        return res
                







        