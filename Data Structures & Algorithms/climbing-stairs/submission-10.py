class Solution:
    def climbStairs(self, n: int) -> int:
        one,two = 1, 1 
        for i in range(n - 1): #n-1很重要 因为n是个数 n-2代表索引
        #i= 0 算的是dp[2]
            temp = one
            one = one + two
            two = temp
        return one

        