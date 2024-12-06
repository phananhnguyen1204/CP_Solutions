class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        cnt = 0
        curr = 0
        ban = set(banned)

        for i in range(1, n + 1):
            if i in ban: continue
            if curr + i > maxSum:
                return cnt
            cnt += 1
            curr += i
        return cnt