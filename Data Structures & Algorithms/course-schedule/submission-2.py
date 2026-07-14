class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
      
        preMap = {i:[] for i in range(numCourses)}
        visit = set()
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        
        def dfs(index):
            if index >= numCourses or index in visit:
                return False
            
            if preMap[index] is None:
                return True
            visit.add(index)
            for pre in preMap[index]:
                if not dfs(pre): return False
            preMap[index] = []
            visit.remove(index)
            return True
        
        for crs in range(numCourses):
            if not dfs(crs): return False
        

        return True
