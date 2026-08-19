class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        
        res = 0
        visit = set()
        rows,cols = len(grid),len(grid[0])

        def bfs(r,c):
            total = 1
            dq = deque()
            dq.append((r,c))
            visit.add((r,c))
            directions = [[1,0],[-1,0],[0,1],[0,-1]]

            while dq:
                row,col = dq.popleft()
                for dr,dc in directions:
                    r,c = row + dr,col + dc
                    if r in range(rows) and c in range(cols) and (r,c) not in visit and grid[r][c] == 1:
                        dq.append((r,c))
                        visit.add((r,c))
                        total += 1
            print(total)
            return total 
        

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r,c) not in visit:
                    res = max(res,bfs(r,c))
        
        return res









