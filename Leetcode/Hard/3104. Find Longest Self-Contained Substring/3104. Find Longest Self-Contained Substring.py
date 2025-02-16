class Solution:
    def maxSubstringLength(self, s: str) -> int:
        """
        add 2 non-overlap self-contained substring
        a: self-contained substring
        b: also self-contained substring
        a + b is a self-contained substring if end = start + 1
        """
        first = defaultdict(int)
        last = defaultdict(int)
        n = len(s)
        intervals = []
        res = -1

        for i in range(n):
            if s[i] not in first:
                first[s[i]] = i
            last[s[i]] = i

        for c, idx in first.items():
            start = idx
            end = last[c]
            valid = True
            for j in range(start, n):
                end = max(last[s[j]], end)
                if first[s[j]] < start:
                    break

                if end == j and end - start + 1 < n: 
                    res = max(end - start + 1,  res)
        
        return res