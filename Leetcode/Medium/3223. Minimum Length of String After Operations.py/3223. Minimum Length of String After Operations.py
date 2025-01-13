class Solution:
    def minimumLength(self, s: str) -> int:
        res = []
        freqs = defaultdict(int)
        """

        "abaacbcbb"
        {   
            a: 3
            b: 4
            c: 2
        }
        """

        for c in s:
            freqs[c] += 1

        for i in range(len(s)):
            count = freqs[s[i]]

            if 0 < count < 3:
                res.append(s[i])
                freqs[s[i]] -= 1
            else:
                freqs[s[i]] -= 2

        print(res)

        return len(res)