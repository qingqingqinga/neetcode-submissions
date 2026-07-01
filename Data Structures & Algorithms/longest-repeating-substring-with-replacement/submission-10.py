class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0

        l = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r],0)
            while (r - l + 1) - max(count.values() ) > k:
                count[s[l]] -= 1
                l += 1
            res = max(res,r - l + 1)
        return res



        res = 0
        count = {}
        l = 0

        for r in range(len(s)):
            count[s[r]] = 1 + count.get(c,0)
            while (r - l + 1) - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res



        for c in s:
            count[c] = 1 + count.get(c,0)

        


















