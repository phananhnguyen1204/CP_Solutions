class Solution:
    def minimumLength(self, s: str) -> int:
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]: return r - l + 1
            while l < r and s[l] == s[l + 1]: l += 1
            while r > l and s[r] == s[r - 1]: r -= 1
            l += 1
            r -= 1
        return 1 if r == l else 0