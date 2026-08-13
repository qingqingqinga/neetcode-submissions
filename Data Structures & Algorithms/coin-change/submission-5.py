class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        #状态定义 dp[a]是这个数额最少需要多少硬币
        #采用自下而上的方式 从dp[0]开始算到dp[n]

        INF = amount + 1 #float('inf')
        dp = [INF] * (amount + 1) #dp[0]也算进去了 0元需要0个硬币
        dp[0] = 0 

        for a in range(1,amount + 1):# a代表的是dp
            for c in coins:
                if a - c >= 0: # a是钱总数 需要大于 硬币面值才有意义
                    dp[a] = min(dp[a],dp[a - c] + 1) # 1代表的是这个coin
 #因为 dp[a] 在进入内层循环之前，就已经记录了一个“不使用当前这枚硬币”时的最优解。
#如果不用 min 把旧值留住，直接赋值覆盖，就会丢失之前算出来的更优答案。

        return dp[amount] if dp[amount] != amount + 1 else -1