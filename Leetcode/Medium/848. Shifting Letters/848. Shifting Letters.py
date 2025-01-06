class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        n = len(s)
        diff = [0] * n

        for i, shift in enumerate(shifts):
            diff[i] += shift

        for i in range(n - 2, -1, -1):
            diff[i] += diff[i + 1]
        
        res = list(s)
        for i in range(n):
            offset = (ord(s[i]) - ord('a') + diff[i]) % 26
            res[i] = chr(offset + ord('a'))

        return "".join(res)