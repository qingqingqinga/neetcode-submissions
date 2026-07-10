class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res  = []
        part = []
        def backtrack(i):
            if i >= len(s):
                res.append(part.copy())
                return
            
            for j in range(i,len(s)):
                if self.isPali(s,i,j):
                    part.append(s[i:j + 1])
                    backtrack(i + 1)
                    part.pop()
        backtrack(0)
        return res


    
   