class Solution:
    def maxScore(self, s: str) -> int:
        cnt_one = s.count('1')
        res = float("-inf")
        left = 0
        for i in range(len(s)-1):
            if s[i] == '1':
                cnt_one -= 1
            else:
                left+=1
            res = max(res, cnt_one + left)
        return res