class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        '''
            in my head this is a bfs,
            basically you just keep checking the specific items

            you do this for every item that is not seen and has

            essentially this is going to only work if there is a path, if there is not a path then we return -1
            

            we will bascially search for the rotten fruit, we will then run the bfs to convert all of the adjacent fruit into also rotten fruit.

            what I'm thinking is that everytime there is a banana and/or rotten item, we add it to the viewed


            basically longest bfs is what i understand, like longest level is waht we return.


            if all the bananas cannot be turned into rotten, then we return -1


            maintain res = 0

            bananaCounter = 0
            state rows ands cols

            seen = set for seen items
            directions = up,down,right,left list
            total = 0

            bfs(r,c):
                declare dq

                while dq:
                    loop through all the items in the dq
                        pop row and col
                        make a for each for the directions to check all sides:
                        if the item is within bounds, hasnt been seen before, equals 1:
                            add it to seen
                            add it to dq
                    total += 
                    
            double for loop here going through rows and cols
                if its a banana then incremeent banana counter

                if its a 2, call bfs,
                
        '''
        q = deque()
        time, fresh = 0,0

        rows,cols = len(grid),len(grid[0])
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append([r,c])
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        while q and fresh > 0:
            for i in range(len(q)):
                r,c = q.popleft()
                for dr,dc in directions:
                    row,col = dr + r, dc + c
                    if row < 0 or row == rows or col < 0 or col== cols or grid[row][col] != 1:
                        continue
                    grid[row][col] = 2
                    q.append([row,col])
                    fresh -= 1
     
            time += 1
        return time if fresh == 0 else -1
                    



        