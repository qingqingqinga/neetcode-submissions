class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = {i:[] for i in range((numCourses))}
        for crs,pre in prerequisites:
            preMap[crs].append(pre)
        visit, cycle = set(),set()
        output = []

        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visit:
                return True
            # 递归 下面的内容其实是假设我们已经拿到pre 我们已经递归完所需要的东西 然后再进行编码
            cycle.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            cycle.remove(crs)
            visit.add(crs)
            output.append(crs)
            return True
        
        for crs in range(numCourses):
            if not dfs(crs):
                return []
        return output
            

        