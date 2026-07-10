class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []          # 存放所有结果组合
        temp = []         # 当前路径

        # 递归函数，参数含义：
        # start: 当前可以选取的起始下标（允许重复选自己）
        # target: 剩余需要凑的目标值
        def dfs(start,target):
            if target == 0:
                res.append(temp.copy())
                return
            if target < 0:
                return
            
            for i in range(start,len(nums)):
                if target - nums[i] >= 0:
                    temp.append(nums[i])
                    dfs(i,target - nums[i])
                    temp.pop()
        dfs(0,target)
        return res

      