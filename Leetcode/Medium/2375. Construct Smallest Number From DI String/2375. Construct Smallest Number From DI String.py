class Solution:
    def smallestNumber(self, pattern: str) -> str:
        """
        IIIDDD
        """
        n = len(pattern)
        res = []
        s = []
        for i in range(n + 1):
            s.append(i + 1)
            while s and (i == n or pattern[i] == 'I'):
                res.append(str(s.pop()))

        return "".join(res)