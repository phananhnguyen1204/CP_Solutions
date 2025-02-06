class Solution:
    def minSteps(self, s: str, t: str) -> int:
        freqs = defaultdict(int)

        n1, n2 = len(s), len(t)
        for c in s:
            freqs[c] += 1

        for c in t:
            freqs[c] -= 1
        
        res = 0
        for char, freq in freqs.items():
            res += abs(freq)

        return res