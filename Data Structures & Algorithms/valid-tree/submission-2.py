class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if n-1 != len(edges):
            return False
        if len(edges) == 0 or not n:
            return True
        
        dic = {i:[] for i in range(n)}
        for start,end in edges:
            dic[start].append(end)
            dic[end].append(start)
        
        seen = set()

        def dfs(cur,prev):
            if cur in seen:
                return False
    
            seen.add(cur)
            for item in dic[cur]:
                if item == prev:
                    continue
                if not dfs(item,cur):
                    return False
            return True

        return dfs(0,-1) and n == len(seen)
