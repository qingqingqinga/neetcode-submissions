class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []          # 存放所有结果组合
        temp = []         # 当前路径

        # 递归函数，参数含义：
        # start: 当前可以选取的起始下标（允许重复选自己）
        # target: 剩余需要凑的目标值
        def dfs(start: int, target: int):
            # 如果剩余目标为 0，说明找到了一组合法组合
            if target == 0:
                res.append(temp.copy())
                return
            # 如果剩余目标小于 0，直接剪枝返回（实际上 for 中已经判断了 >=0，此处可省略）
            if target < 0:
                return

            # 从 start 开始遍历候选数
            for i in range(start, len(nums)):
                # 如果当前数字能减（即 <= 剩余目标），则尝试选取
                if target - nums[i] >= 0:
                    temp.append(nums[i])
                    # 递归时传入 i（而不是 i+1），允许重复使用同一个数字
                    dfs(i, target - nums[i])
                    # 回溯，移除刚才添加的数字
                    temp.pop()

        dfs(0, target)
        return res