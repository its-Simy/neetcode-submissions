class Solution:


#issue one, how do i know hwo to seperate each string in the list


    def encode(self, strs: List[str]) -> str:
        answer = ""
        #loop through the lis
        #find how big the item is in list
        #add to the list size#(item)

        for x in strs:
            answer += str(len(x)) + "#" + x
        
        return answer

    def decode(self, s: str) -> List[str]:
        answer = []
        i = 0
        while i < len(s):
            j = s.find("#", i)
            length = int(s[i:j])
            answer.append(s[j + 1 : j + 1 + length])
            i = j + 1 + length

        return answer

       