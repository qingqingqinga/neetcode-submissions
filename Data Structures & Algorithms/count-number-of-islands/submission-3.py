class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        res = 0

        directions = [[1,0],[-1,0],[0,1],[0,-1]]

        def dfs(row,col):
            if (row < 0 or row >= rows or col < 0 or col >= cols or grid[row][col] == "0"):
                return 

            grid[row][col] = "0" #一定要记得 return之后要缩进正确

            for dr, dc in directions:
                move_row,movw_col = dr + row,dc + col
                dfs( move_row,movw_col)



        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    res += 1
                    dfs(i,j)
                    
        return res

        


        