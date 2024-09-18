class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_cnt = {}
        s2_cnt = {}
        l = 0
        for c in s1:
            s1_cnt[c] = s1_cnt.get(c, 0) + 1
        for r in range(len(s2)):
            s2_cnt[s2[r]] = s2_cnt.get(s2[r], 0) + 1
            if r >= len(s1):
                s2_cnt[s2[l]] -= 1
                if s2_cnt[s2[l]] == 0: del s2_cnt[s2[l]]
                l += 1
            if s1_cnt == s2_cnt: return True
        return False
