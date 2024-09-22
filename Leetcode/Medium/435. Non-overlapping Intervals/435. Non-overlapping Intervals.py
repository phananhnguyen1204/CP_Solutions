class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        res = 0
        intervals.sort()
        print(intervals)
        prevEnd = intervals[0][1]
        for i in range(1, len(intervals)):
            if intervals[i][0] < prevEnd:
                res += 1
                prevEnd = min(prevEnd, intervals[i][1])
            else:
                prevEnd = intervals[i][1]
        return res
