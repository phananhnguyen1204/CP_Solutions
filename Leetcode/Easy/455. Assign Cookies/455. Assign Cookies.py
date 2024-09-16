class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        if len(s) == 0: return 0
        g.sort()
        s.sort()
        res = 0

        j = 0
        for i in range(len(s)):
            if g[j] <= s[i]:
                res += 1
                j += 1
            
            if j == len(g): break
        return res