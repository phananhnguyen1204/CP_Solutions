class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l = 0
        minLen = float("inf")
        res = ""
        cntT, cntS = {}, {}
        for c in t:
            cntT[c] = cntT.get(c, 0) + 1
        
        def check():
            for key in cntT:
                if cntS.get(key, 0) < cntT[key]: return False
            return True

        for r in range(len(s)):
            cntS[s[r]] = cntS.get(s[r], 0) + 1
            while check():
                if minLen > (r - l + 1):
                    minLen = r - l + 1
                    res = s[l : r + 1]
                
                cntS[s[l]] -= 1
                l += 1
        return res
            