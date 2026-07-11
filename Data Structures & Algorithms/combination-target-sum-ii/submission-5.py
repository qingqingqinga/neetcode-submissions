class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        res = []
        path = []

        candidates.sort()

        def backtrack(i,target):
            if target == 0:
                res.append(path.copy())
                return
            
            if i >= len(candidates) or target < 0: #题目要求不重复 所以一定会在长度之内找到
                return
            
            if target - candidates[i] >= 0:
                path.append(candidates[i])
                backtrack(i + 1,target - candidates[i])
                path.pop()
                while (i + 1) < len(candidates) and candidates[i] == candidates[i + 1]:
                    i += 1
                backtrack(i + 1,target)
        backtrack(0,target)
        return res
        #这题是一个融合subset子集 和不重复 以及组合题target的题
        