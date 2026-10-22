class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''
        
        '''

        dic = {}

        for i in strs:
            q = "".join(sorted(i))
            
            if q in dic:
                dic[q].append(i)
            else:
                dic[q] = [i]

        res = []
        for i in dic.values():
            res.append(i)
        
        return res

