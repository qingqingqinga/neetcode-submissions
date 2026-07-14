class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
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

        