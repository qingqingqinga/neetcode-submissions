class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
            



        # 获取网格的行数和列数
        rows = len(board)
        cols = len(board[0])

        # 创建访问记录表，初始全为 False
        visited = [[False] * cols for _ in range(rows)]

        # 定义深度优先搜索函数（嵌套函数，可以访问外部变量）
        def dfs(row: int, col: int, index: int) -> bool:
            # 如果已经匹配到 word 的最后一个字符之后，说明找到了完整路径
            if index == len(word):
                return True

            # 边界检查：越界、字符不匹配、已经被访问过 → 这条路不通
            if (row < 0 or row >= rows or col < 0 or col >= cols or
                board[row][col] != word[index] or visited[row][col]):
                return False

            # 当前格子符合条件，标记为已访问
            visited[row][col] = True

            # 尝试四个方向：上、下、左、右（递归）
            # 只要有一个方向能走通，就返回 True
            if (dfs(row - 1, col, index + 1) or
                dfs(row + 1, col, index + 1) or
                dfs(row, col - 1, index + 1) or
                dfs(row, col + 1, index + 1)):
                return True

            # 四个方向都走不通，回溯：取消当前格子的访问标记
            visited[row][col] = False
            return False

        # 遍历整个网格的每个格子，作为搜索起点
        for i in range(rows):
            for j in range(cols):
                if dfs(i, j, 0):   # 从索引 0 开始匹配
                    return True

        # 所有起点都试过，没有找到
        return False       