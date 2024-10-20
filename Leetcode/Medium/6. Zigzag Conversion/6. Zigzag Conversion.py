class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if len(s) == 1 or numRows == 1: return s
        i = 0
        tmp = [""] * numRows
        idx = 0
        down = True
        while i < len(s):
            tmp[idx] += s[i]
            if idx == 0:
                down = True
            if idx == numRows - 1:
                down = False
            idx += 1 if down else -1
            i += 1
        return "".join(tmp)
