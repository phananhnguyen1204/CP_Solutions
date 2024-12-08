class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        events.sort(key = lambda x: x[0])

        n = len(events)
        res = float("-inf")
        suffix = [0] * n
        suffix[n-1] = events[n-1][2]

        for i in range(n-2, -1, -1):
            suffix[i] = max(events[i][2], suffix[i+1])

        for i, event in enumerate(events):
            start, end, val = event

            next_event_index = -1
            l, r = i + 1, n - 1
            
            while l <= r:
                mid = (l + r) // 2
                if events[mid][0] > end:
                    next_event_index = mid
                    r = mid - 1
                else:
                    l = mid + 1

            if next_event_index != -1:
                res = max(res, val + suffix[next_event_index])
            res = max(res, val)

        return res