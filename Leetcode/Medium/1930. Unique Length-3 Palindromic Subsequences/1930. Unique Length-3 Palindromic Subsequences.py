class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        first = [-1] * 26
        last = [-1] * 26

        for i in range(len(s)):
            c = s[i]
            if first[ord(c) - ord('a')] == -1:
                first[ord(c) - ord('a')] = i
            last[ord(c) - ord('a')] = i
        res = 0
        for i in range(26):
            if first[i] == -1: 
                continue
            between = set()
            for j in range(first[i]+1, last[i]):
                between.add(s[j])
            res += len(between)
        return res