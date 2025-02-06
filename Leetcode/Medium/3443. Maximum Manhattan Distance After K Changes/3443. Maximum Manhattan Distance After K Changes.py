class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        
        """
        NSEW
        x: 0
        y: 1

        NSWWEW
        x: 2 
        y:0
        """

        freqs = defaultdict(int)
        res = 0
        for c in s:
            freqs[c] += 1
            curr_dist = 0
            h, v = min(freqs['W'], freqs['E']), min(freqs['N'], freqs['S'])

            if v + h <= k: 
                curr_dist = freqs['W'] + freqs['E'] + freqs['N'] + freqs['S']
            elif h <= k:
                remain = k - h
                curr_dist = freqs['W'] + freqs['E'] + max(freqs['S'], freqs['N']) + 2 * remain - v
            # h > k
            else:
                curr_dist = abs(freqs['S'] - freqs['N']) + abs(freqs['W'] - freqs['E']) + 2 * k
            res = max(res, curr_dist)

        return res
