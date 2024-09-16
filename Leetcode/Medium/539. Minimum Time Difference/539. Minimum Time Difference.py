class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        minutes = [ int(time[:2]) * 60 + int(time[3:]) for time in timePoints ]
        minutes.sort()
        res = float("inf")
        for i in range(1, len(minutes)):
            res = min(minutes[i] - minutes[i-1], res)
        return min(res, 24 * 60 - minutes[-1] + minutes[0])