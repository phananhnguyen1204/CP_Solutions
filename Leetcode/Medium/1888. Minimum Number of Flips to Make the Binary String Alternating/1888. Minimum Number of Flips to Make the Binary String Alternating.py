class Solution:
    def minFlips(self, s: str) -> int:
        '111010'
        '1010101010'
        n = len(s)
        s = s + s
        alter1 , alter2 = "", ""
        for i in range(2 * n):
            if i % 2 == 0:
                alter1 += "1"
                alter2 += "0"
            else:
                alter1 += "0"
                alter2 += "1"
        l = 0
        res = n
        diff1, diff2 = 0, 0
        for r in range(len(s)):
            if s[r] != alter1[r]: diff1 += 1
            if s[r] != alter2[r]: diff2 += 1
            if r - l + 1 == n:
                res = min(res, diff1, diff2)
                if s[l] != alter1[l]: diff1 -= 1
                if s[l] != alter2[l]: diff2 -= 1
                l += 1
        return res

        