class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        '''
            if both open and close equal n
                append to the res

            we are basically going to say that as long as open doesn't equal n
                append open
                increment open
                call the next function
            if string exists:
                pop last item of the string
            
            if close < open:
                append close
                increment close
                call the next fucntion
        '''

        res = []

        def par(current, o, close):
            print("Current: ",current," open: ",o, " Close: ", close)
            if o == n and close == n:
                res.append(current)
                return
            temp = current
            if o != n:
                par(current + "(",o + 1,close)
            current = temp
            if close < o:
                par(current + ")",o,close + 1)
        par("",0,0)
        return res
            


        