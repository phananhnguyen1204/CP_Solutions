class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        n = len(s1)
    

        freq = defaultdict(int)

        for i in range(n):
            freq[s1[i]] += 1
            freq[s2[i]] -= 1

        cnt = 0
        for i in range(n):
            if s1[i] != s2[i]:
                cnt += 1
            if freq[s1[i]] != 0 or freq[s2[i]] != 0: return False

        return cnt == 2 or cnt == 0