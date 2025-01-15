class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        """
        len(s) == len(t)
        maxCost > len(s) -> can change s to t
        maxCost == 0 -> 2 strings must be the same
        -> sliding window
        """

        res = l = 0
        n = len(s)
        cost = 0
        
        for r in range(n):
            if s[r] != t[r]:
                cost += abs(ord(t[r]) - ord(s[r]))
            while cost > maxCost:
                cost -= abs(ord(t[l]) - ord(s[l]))
                l += 1
            res = max(res, r - l + 1)
        return res
        