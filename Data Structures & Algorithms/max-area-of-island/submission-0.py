class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_len = 0
        rows = len(grid)
        cols = len(grid[0])

        def dfs(row,col) -> int:
            if (row < 0 or row >= rows or col < 0 or col >= cols or grid[row][col] == 0):
                return 0 #需要返回值
            
            grid[row][col] = 0

            area = 1

            area += dfs(row - 1,col)
            area += dfs(row + 1,col)
            area += dfs(row,col + 1)
            area += dfs(row,col - 1)
            return area

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    max_len = max(max_len,dfs(i,j))
                    
        return max_len

        


            



        
        