class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        res = 0
        dic = {i:[] for i in range(n)}
        for start,end in edges:
            dic[start].append(end)
            dic[end].append(start)

        check = {i:0 for i in range(n)}
        seen = set()

        def dfs(cur):
            if cur in seen or dic[cur] == []:
                return
            if check[cur] ==  0:
                check[cur] = 1
            
            seen.add(cur)
            for item in dic[cur]:
                dfs(item)
            dic[cur] = []


        for item in range(n):
            if check[item] == 0:
                res += 1
                dfs(item)
        
        return res