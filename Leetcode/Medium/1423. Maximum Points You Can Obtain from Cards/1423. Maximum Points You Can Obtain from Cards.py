class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        len_required = n - k

        remain_sum = float("inf")
        start = 0
        curr_sum = 0

        if k == n:
            return sum(cardPoints)

        for end in range(n):
            curr_sum += cardPoints[end]
            if end - start + 1 == len_required:
                remain_sum = min(remain_sum, curr_sum)
                curr_sum -= cardPoints[start]
                start += 1
        return sum(cardPoints) - remain_sum
