class Solution:
    def maxDepth(self, s: str) -> int:
        res = 0
        cnt = 0
        for c in s:
            if c == '(':
                cnt += 1
            elif c == ')':
                cnt -= 1
            res = max(res, cnt)
        return res