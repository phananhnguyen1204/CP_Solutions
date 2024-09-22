class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        '''
        [1, 2] [3, 10] [1, 11] [9, 15]
        '''
        if not intervals: return 0
        intervals.sort()
        minHeap = []
        heapq.heappush(minHeap, intervals[0][1])
        for i in range(1, len(intervals)):
            if intervals[i][0] >= minHeap[0]:
                heapq.heappop(minHeap)
            heapq.heappush(minHeap, intervals[i][1])
        return len(minHeap)
