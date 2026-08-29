class Solution:
    def validPalindrome(self, s: str) -> bool:
        if len(s) == 1 or len(s) == 2:
            return True
        
        def is_palindrome(s):
            return s == s[::-1]
        l, r = 0, len(s) - 1
        
        if is_palindrome(s):
            return True
        
        while l <= r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                s1 = s[:l] + s[l + 1:]
                s2 = s[:r] + s[r + 1:]
                if is_palindrome(s1) or is_palindrome(s2):
                    return True
                else:
                    return False

