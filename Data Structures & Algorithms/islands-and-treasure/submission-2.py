class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        visit = set()
        q = deque()
        
        def addLand(r, c):
            if (r < 0 or r == rows or c < 0 or c == cols or
                (r, c) in visit or grid[r][c] == -1):
                return
            visit.add((r, c))
            q.append([r, c])

        
        # 将所有宝藏（0）加入队列
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append([r, c]) #队列用 [r, c]：因为队列存储什么类型都可以，用列表是习惯

                    visit.add((r,c))   #集合用 (r, c)：因为必须用元组，列表不能放入集合 #
                                  
                    
        
        dist = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft() #里面是元组 弹出来出来然后解包成两个对象
                grid[r][c] = dist
                addLand(r + 1, c)
                addLand(r - 1, c)
                addLand(r, c - 1)
                addLand(r, c + 1)
            dist += 1

