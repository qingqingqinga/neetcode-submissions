class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def backtrack(start: int, comb: List[int]) -> None:
            # 1. 终止条件
            if len(comb) == k:
                res.append(comb.copy())
                return
            
            # 3. 遍历选择列表并执行选择-探索-撤销
            for i in range(start, n + 1):
                comb.append(i)          # 选择
                backtrack(i + 1, comb)  # 探索（i+1 确保组合无序）
                comb.pop()              # 撤销（状态重置）
        
        backtrack(1, [])
        return res
        