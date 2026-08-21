class Solution:
    def numDecodings(self, s: str) -> int:
      

        #dp[i]：表示前 i 个字符（即 s[0:i]）的解码方案数。
        #dp[i] = ((dp[i - 1]) if  dp[i - 1] != '0' else 0 ) 
                #+ (dp[i - 2]) if s[i - 2: i] 属于 10 - 26
        
        n = len(s)
        if n == 0 or s[0] == '0':
            return 0

        # 初始化：dp[0] = 1（空串），dp[1] = 1（如果第一个字符非零）
        prev2 = 1 #重点         # 对应 dp[i-2]，初始为 dp[0]
        prev1 = 1   # 对应 dp[i-1]，初始为 dp[1]
      
        #i 代表 “当前正在计算的字符串长度 i=2 是在计算两个字符的时候的解码数量
        # i代表虚拟的12的第三个台阶
        # i = 2（我们要计算前 2 个字符 "22" 的方案数 dp[2]）
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