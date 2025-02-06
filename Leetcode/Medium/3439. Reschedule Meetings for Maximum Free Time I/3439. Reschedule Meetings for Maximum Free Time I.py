class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
        """
        greedy
        can reschedule at most k meeting -> k + 1 gaps
        max free time = total of gaps

        to maximize longest continuous period of free time
        -> consider reschedule a subarray evens of size k
        """
        n = len(startTime)
        gaps = [0] * (n + 1)

        prevEnd = 0
        for i in range(n):
            if i == 0: gaps[i] = startTime[i] - prevEnd
            else: gaps[i] = startTime[i] - prevEnd + gaps[i-1]
            prevEnd = endTime[i]
        # handle last gap
        gaps[n] = eventTime - prevEnd + gaps[n-1]

        l = 0
        res = 0
        for r in range(n):
            # len of reschedule event >= k
            # start shrinking the window
            if r - l + 1 >= k:
                res = max(res, gaps[r + 1] - gaps[l - 1]) if l > 0 else max(res, gaps[r + 1])
                l += 1
        return res
 

