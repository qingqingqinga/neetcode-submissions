class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:


        l = 0
        res = 0
        hashmap = set()
        for r in range(l,len(s)):
            while s[r] in hashmap:
                hashmap.remove(s[l])
                l += 1
                
            hashmap.add(s[r])
            res = max(r - l + 1,res)
        return res

