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
                    backtrack(j + 1) #这里从j + 1开始而不是i + 1，因为之前已经处理过j之前的片段了 可能i到j的片段大于1
                    part.pop()
        backtrack(0)
        return res
    def isPali(self,s,l,r):#错误点：全局的函数必须要有self TypeError: Solution.isPali() takes 3 positional arguments but 4 were given
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True


    
   