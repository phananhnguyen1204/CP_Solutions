from heapq import heappush, heappop
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def dis(x, y):
            return x ** 2 + y ** 2
        maxHeap = []
        for i, point in enumerate(points):
            x, y = point
            heappush(maxHeap, (- dis(x, y), point))
            if len(maxHeap) > k:
                heappop(maxHeap)
        return [point for _, point in maxHeap]
        