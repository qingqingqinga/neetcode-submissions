class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
# 最大子数组和 = cur - 最小前缀和 所以前缀和要最小
   
       
        min_pre = 0  # 空前缀
        cur = 0
        res = float('-inf')
        for num in nums:
            cur += num
            res = max(res, cur - min_pre)  # 当前前缀和 - 历史最小前缀和
            min_pre = min(min_pre, cur)    # 更新历史最小前缀和
        return res

        

