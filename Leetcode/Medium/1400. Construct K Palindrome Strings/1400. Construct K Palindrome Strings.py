class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        """
        aba
        cc
        dd
        """
        freqs = defaultdict(int)
        count_odd = 0
        
        for c in s:
            freqs[c] += 1
            
        for char, count in freqs.items():
            if count % 2 == 1:
                count_odd += 1
            if count_odd > k:
                return False
        
        return k <= len(s)

        