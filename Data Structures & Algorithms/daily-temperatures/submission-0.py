class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        '''
            this could be solved with a double for loop
        '''

        res = []

        for i in range(len(temperatures)):
            check = len(res)
            for j in range(i + 1,len(temperatures)):
                if temperatures[j] > temperatures[i]:
                    res.append(j-i)
                    break

            if len(res) == check:
                res.append(0)

        return res