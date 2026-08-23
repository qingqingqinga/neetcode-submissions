class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque() #重点 因为可能有两个橘子同时腐烂 只用dfs的话 是一个一个橘子计算的不行 #bfs一般不用回溯dfs
        rows = len(grid)
        cols = len(grid[0])

        time = 0

        fresh = 0 #判断是否能腐烂完所有橘子


        for i in range(rows):
            for j in range(cols): #存下fresh 和初始化队列
                if grid[i][j] == 2:
                    q.append([i,j])
                if grid[i][j] == 1:
                    fresh += 1

        directions = [[1,0],[-1,0],[0,-1],[0,1]] #四个方向腐烂
        
        while q and fresh > 0:
            n = len(q)
            for _ in range(n):
                i,j = q.popleft() #一定要用popleft而不是pop
                for dr, dc in directions:
                    row,col = dr + i,dc + j #不能i,j = dr + i,dc + j 这样i，j会影响后续方向
                    if (row < 0 or row >= rows or col < 0 or col >= cols or grid[row][col] != 1): #经常会写错
                        continue #不能return 要不然后序橘子都不计算了
                    grid[row][col] = 2
                    q.append([row,col])
                    fresh -= 1
            time += 1 #要记得
        
        return time if fresh == 0 else -1
                


        q = deque()
        rows, cols = len(grid), len(grid[0])
        time, fresh = 0, 0

        

        def addOrange(r: int, c: int) -> None:
            nonlocal fresh
            # 检查边界和是否为新鲜橘子
            if (r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] != 1):
                return
            # 标记为腐烂
            grid[r][c] = 2
            q.append([r, c])
            fresh -= 1

        # 1. 统计新鲜橘子，腐烂橘子入队
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append([r, c])
        
        # 2. BFS 逐层腐烂
        while q and fresh > 0:
            for _ in range(len(q)):
                r, c = q.popleft()
                # 四个方向尝试感染
                addOrange(r - 1, c)  # 上
                addOrange(r + 1, c)  # 下
                addOrange(r, c - 1)  # 左
                addOrange(r, c + 1)  # 右
            time += 1

        return time if fresh == 0 else -1

        