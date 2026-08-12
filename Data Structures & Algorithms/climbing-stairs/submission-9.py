class Solution:
    def climbStairs(self, n: int) -> int:
        one,two = 1, 1 
        for i in range(n - 1): #n-1很重要 因为n是个数 n-1代表索引
            temp = one
            one = one + two
            two = temp
        return one
        