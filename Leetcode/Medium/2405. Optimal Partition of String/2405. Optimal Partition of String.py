class Solution:
    def partitionString(self, s: str) -> int:
        res = 0
        unique = set()
        n = len(s)
        for i in range(n):
            if s[i] not in unique:
                unique.add(s[i])
                continue
            
            unique = {s[i]}
            res += 1
        res += 1
        return res 