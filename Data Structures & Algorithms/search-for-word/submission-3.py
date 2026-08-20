class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows,cols = len(board),len(board[0])
        self.res = False


        def dfs(curWord,seen,r,c,pointer):
            directions = [[1,0],[-1,0],[0,1],[0,-1]]
            if curWord == word:
                self.res = True
                return

            for dr,dc in directions:
                nr,nc = r + dr, c + dc
                if nr in range(rows) and nc in range(cols) and (nr,nc) not in seen and pointer < len(word) and board[nr][nc] == word[pointer]:
                    if curWord + board[nr][nc] == word:
                        self.res = True
                        return
                    seen.add((nr,nc))
                    dfs(curWord + board[nr][nc],seen,nr,nc,pointer + 1)
                    seen.remove((nr,nc))


        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0]:
                    temp = set()
                    temp.add((r,c))
                    check = dfs("" + word[0],temp,r,c,1)
        return self.res
        