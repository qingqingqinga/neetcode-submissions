class Solution:
    def climbStairs(self, n: int) -> int:
        prev1, prev2 = 1,1
        for i in range(2,n + 1):
        
            curr = prev1 + prev2   # 计算 dp[i]
            prev2 = prev1          # 更新 dp[i-2] = 旧的 dp[i-1]
            prev1 = curr           # 更新 dp[i-1] = 当前的 dp[i]
        return prev1

        #dp[i] = dp[i - 1] + dp[ i - 2]
    
