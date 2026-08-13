class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)

        
        #dp[i] = ((dp[i - 1] + 1) if  dp[i - 1] != '0' else 0 ) 
                #+ (dp[i - 2] + 1) if s[i - 2: i] 属于 10 - 26
        
        n = len(s)
        if n == 0 or s[0] == '0':
            return 0

        # 初始化：dp[0] = 1（空串），dp[1] = 1（如果第一个字符非零）
        prev2 = 1          # 对应 dp[i-2]，初始为 dp[0]
        prev1 = 1 if s[0] != '0' else 0   # 对应 dp[i-1]，初始为 dp[1]

        # 从第 2 个字符开始迭代（i 从 2 到 n）
        for i in range(2, n + 1):
            curr = 0

            # 1）单个字符解码（对应爬楼梯的走 1 步）
            if s[i-1] != '0':
                curr += prev1

            # 2）两个字符组合解码（对应爬楼梯的走 2 步）
            two_digit = int(s[i-2:i])   # 取 s[i-2] 和 s[i-1] 组成的数字
            if 10 <= two_digit <= 26:
                curr += prev2

            # 滚动更新（和爬楼梯一模一样）
            prev2, prev1 = prev1, curr

        return prev1       