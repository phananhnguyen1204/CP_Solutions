from heapq import heappush, heappop
class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        minHeap = []
        freq = {}

        for x in arr:
            freq[x] = freq.get(x, 0) + 1
        
        for key, val in freq.items():
            heappush(minHeap, (val, key))

        for i in range(k):
            val, key = heappop(minHeap)
            val -= 1
            if val > 0:
                heappush(minHeap, (val, key))

        return len(minHeap)