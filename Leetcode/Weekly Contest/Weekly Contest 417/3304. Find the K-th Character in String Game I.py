class Solution:
    def kthCharacter(self, k: int) -> str:
        s = "a"
        while True:
            for c in s:
                tmp = s
                if c == 'z':
                    s += 'a'
                else:
                    s += chr(ord(c) + 1)
            if len(s) >= k:
                break
        return s[k - 1]
        