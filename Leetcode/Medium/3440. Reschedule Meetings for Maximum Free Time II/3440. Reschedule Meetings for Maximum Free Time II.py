class Solution:
    def maxFreeTime(self, eventTime: int, startTime: List[int], endTime: List[int]) -> int:
        """
        schedule only 1 event ->
        max free time = sum of both gaps between the rescheduled event (true if order stay the same)

        however, IMPORTANT: the relative order of all meetings does not stayd the same.
        but how to reschedule?

        if there is available gap from the left or right -> just move it to maximize free time
        """

        res = 0
        n = len(startTime)
        prevEnd = 0
        nextStart = 0
        max_available_gap = 0
        gaps = []

        for i in range(n):
            gaps.append(startTime[i] - prevEnd)
            prevEnd = endTime[i]
        gaps.append(eventTime - endTime[n - 1])

        for i in range(n):
            free_time = gaps[i + 1] + gaps[i]

            if max_available_gap >= (endTime[i] - startTime[i]):
                free_time += endTime[i] - startTime[i] 
            res = max(free_time, res)
            max_available_gap = max(max_available_gap, gaps[i])

        max_available_gap = 0
        for i in range(n-1, -1, -1):
            free_time = gaps[i + 1] + gaps[i]

            if max_available_gap >= (endTime[i] - startTime[i]):
                free_time += endTime[i] - startTime[i] 
            res = max(free_time, res)
            max_available_gap = max(max_available_gap, gaps[i + 1])

        return res

            
        
            

