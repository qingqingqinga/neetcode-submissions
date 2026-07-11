class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        #剪掉的枝：
        #整个右子树中所有以"不选第一个1"开头的路径中的 "选第二个1" 分支
        #如果我们不选1 那第二个的1也不能选 直接跳过
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        res = []
        path = []

        nums.sort()

        def dfs(i):
            if i >= len(nums):
                res.append(path.copy())
                return
            
            path.append(nums[i])
            dfs(i + 1)

            path.pop()

            while (i + 1) < len(nums) and nums[i] == nums[i + 1]: #一定不能while (i + 1) <= len(nums)等于代表已经越界了
                i += 1
            
            dfs(i + 1)
        dfs(0)
        return res
        