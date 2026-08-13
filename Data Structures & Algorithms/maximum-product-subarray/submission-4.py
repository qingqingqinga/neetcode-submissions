class Solution:
    def maxProduct(self, nums: List[int]) -> int:
         # 初始化：res 先取数组第一个值（如果数组为空则需特殊处理，但题目保证非空）
        res = nums[0]
        curMax, curMin = 1, 1
        for n in nums:
            # 特殊处理 0：重置状态，但 0 本身作为子数组需要保留在 res 中
            if n == 0:
                curMax, curMin = 1, 1
                res  = max(0,res) #非常重要不能漏掉
                continue

            # 保存旧的最大值，因为计算 min 时需要旧值
            tmp = curMax * n

            # 状态转移：当前元素 n 有“重新开始”或“接在后面”两种本质动作
            curMax = max(n, n * curMax, n * curMin)
            curMin = min(n, tmp, n * curMin)

            # 更新全局最优
            res = max(res, curMax)

        return res
