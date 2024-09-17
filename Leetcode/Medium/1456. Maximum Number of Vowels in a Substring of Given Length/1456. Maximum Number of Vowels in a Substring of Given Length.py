class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        res = 0
        cnt = 0
        vowels = {'a', 'e', 'u', 'i', 'o'}
        for i in range(k-1):
            if s[i] in vowels: cnt += 1
        res = cnt
        l = 0
        for i in range(k - 1, len(s)):
            if s[i] in vowels: cnt += 1
            res = max(res, cnt)
            if s[l] in vowels: cnt -= 1
            l += 1
        return res
        