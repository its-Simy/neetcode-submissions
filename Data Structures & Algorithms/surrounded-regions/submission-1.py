class Solution:
    def solve(self, board: List[List[str]]) -> None:
        '''
        bascially we can run a dfs here

        we have to guarantee that a region is fully surrounded
            we can do that by basically checking the whole surrounded area, if any of those equal a O, then we will run a dfs on it and add it to visited on all four directions as long as its in bounds, after we basiscally just brute force parse through and make sure we adjust the rest of the "enclosed" regions
        '''
        visited = set()
        rows,cols = len(board),len(board[0])

        def dfs(r,c):
            if (r,c) in visited or r < 0 or c < 0 or r == rows or c == cols or board[r][c] == 'X':
                return
            print("visited: R: ",r," C: ",c)
            visited.add((r,c))
            dfs(r + 1,c)
            dfs(r - 1,c)
            dfs(r,c + 1)
            dfs(r,c - 1)

        for r in range(rows):
            if board[r][0] == 'O':
                dfs(r,0)
            if board[r][cols-1] == 'O':
                dfs(r,cols-1)
        for c in range(cols):
            if board[0][c] == 'O':
                dfs(0,c)
            if board[rows-1][c] == 'O':
                dfs(rows-1,c)

        print(visited)
        for r in range(rows):
            for c in range(cols):
                if (r,c) not in visited and board[r][c] == 'O':
                    board[r][c] = 'X'