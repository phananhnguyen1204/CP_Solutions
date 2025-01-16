class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        """
        invalid frog: freq of next char > freq of prev char in "croak"
        """

        res = 0
        freqs = defaultdict(int)

        for c in croakOfFrogs:
            freqs[c] += 1

            if freqs['k'] <= freqs['a'] <=freqs['o'] <= freqs['r'] <= freqs['c']:
                res = max(res, freqs['c'] - freqs['k'])
            else:
                return -1

        if freqs['k'] == freqs['a'] ==freqs['o'] == freqs['r'] == freqs['c']:
            return res

    
        return -1
        