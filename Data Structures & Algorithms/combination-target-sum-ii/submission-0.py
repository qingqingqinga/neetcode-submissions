class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        path = []
        candidates.sort()

        def dfs(i,target):
            if target == 0:
                res.append(path.copy())
                return
            
            if i >= len(candidates) or target < 0:
                return
            
            path.append(candidates[i])
            backtrack(i + 1,path)
            path.pop()
            while (i + 1) < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            backtrack(i + 1,path)
        dfs(0,target)
        return res
        