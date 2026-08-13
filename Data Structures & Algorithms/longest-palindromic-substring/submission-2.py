class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""#相当于哨兵 len（res）不可以是none
        n = len(s)
        if n == 1:
            return s[0]
        for i in range(len(s)):
            l,r = i, i 
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            if (r - 1) - (l + 1) + 1 > len(res): #在 while 循环的外部，此时 l 和 r 已经执行完最后一次 l-=1 和 r+=1，跑过头了
                    res = s[l + 1 : r ]
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
               
                l -= 1
                r += 1
            if r - l - 1 >len(res):
                res = s[l + 1: r]
        return res
            
