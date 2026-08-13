class Solution:
    def rob(self, nums: List[int]) -> int:
       
        #dp[i] = max(dp[i - 2] + dp[i],dp[i - 1])
        


        
        n = len(nums)
        # 边界条件：空数组（虽然题目一般保证非空，但为健壮性保留）
        if n == 0:
            return 0
        # 边界条件：仅有一间房屋
        if n == 1:
            return nums[0]
        
        # 初始化：dp[0] 和 dp[1]
        prev2 = nums[0]                     # 对应 dp[i-2]
        prev1 = max(nums[0],nums[1])      # 对应 dp[i-1]
        
        # 递推：从第 2 间房屋开始迭代
        for i in range(2, n):
            curr = max(prev1, prev2 + nums[i])
            # 状态滚动（右移）
            prev2 = prev1
            prev1 = curr
            
        return prev1
        