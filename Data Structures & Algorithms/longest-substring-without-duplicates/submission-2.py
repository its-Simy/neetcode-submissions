class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
            looking for the longest substring without duplicates
            return an int


            concerns:
                how to know what I already have????
                    use the find method?

            resets by moving the left pointer up to the right pointer, using a while

            keep track of best length of subset
            keep track of the best
            left,right pointer

            while r < length
                if find function of (slicing between left and right pointer) doesnt return -1
                    move the left pointer to where the right pointer is
                    reset count
                if count is better than the best:
                    update best
                update right pointer
                update count
        '''

        left,right,current,best= 0,0,"",0

        while right < len(s):
            while current.find(s[right]) != -1:
                left +=1
                current = s[left:right]
            current = s[left:right+1]
            best = max(best,len(current))
                
                
            right += 1
            
            
            
            
            
        
        return best










         
        