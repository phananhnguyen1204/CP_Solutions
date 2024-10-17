from heapq import heappush, heappop
class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        max_heap = []
        if a != 0:
            heappush(max_heap, (-a, "a"))
        if b != 0:
            heappush(max_heap, (-b, "b"))
        if c != 0:
            heappush(max_heap, (-c, "c"))

        res = ""
        while max_heap:
            cnt, curr = heappop(max_heap)
            if len(res) >= 2 and res[-1] == res[-2] == curr:
                if not max_heap: break
                cnt2, curr2 = heappop(max_heap)
                cnt2 += 1
                res += curr2
                if cnt2 < 0:
                    heappush(max_heap, (cnt2, curr2))
                heappush(max_heap, (cnt, curr))
            else:
                cnt += 1
                res += curr
                if cnt < 0:
                    heappush(max_heap, (cnt, curr))
        
        return res


        