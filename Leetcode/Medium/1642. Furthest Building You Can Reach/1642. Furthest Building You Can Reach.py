from heapq import heappush, heappop
class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        res = 0
        # max_heap
        bricks_allocation = []

        for i in range(len(heights) - 1):
            diff = heights[i + 1] - heights[i]
            if diff < 0:
                continue
            bricks -= diff
            heappush(bricks_allocation, -diff)
            if(bricks < 0):
                if ladders == 0:
                    return i
                else:
                    ladders -= 1
                    bricks += -heappop(bricks_allocation)
        return len(heights) - 1
            
