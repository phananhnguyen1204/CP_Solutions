class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        n1, n2 = len(s), len(p)
        start = 0
        p_cnt = {}
        s_cnt = {}
        for c in p:
            p_cnt[c] = p_cnt.get(c,0) + 1
        
        res = []
        for end in range(n1):
            s_cnt[s[end]] = s_cnt.get(s[end], 0) + 1
            if end >= n2:
                s_cnt[s[start]] -= 1
                if s_cnt[s[start]] == 0: del s_cnt[s[start]]
                start += 1
            if s_cnt == p_cnt: res.append(end - n2 + 1)
        return res