class Solution:
    def validPalindrome(self, s: str) -> bool:
        n = len(s)
        l, r = 0, n - 1
        def check(l, r):
            while l <= r:
                if s[l] == s[r]:
                    l += 1 
                    r -= 1
                    continue
                return False
            return True
        while l <= r:
            if s[l] == s[r]:
                l += 1
                r -= 1
                continue
            return check(l + 1,r) or check(l, r - 1)
        return True