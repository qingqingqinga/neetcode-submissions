class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n + 1)

        for i in range(n + 1):
            dp[i] = dp[i >> 1] + (i & 1) #dp[i] = dp[i // 2] + (i % 2)
        return dp
        
        

        
        res = []
        for i in range(n + 1):
            count = 0
            while i:
                i &= i - 1
                count += 1
            res.append(count)
        return res

        