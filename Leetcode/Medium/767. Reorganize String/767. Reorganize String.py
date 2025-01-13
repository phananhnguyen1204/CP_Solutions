from heapq import heappush, heappop
class Solution:
    def reorganizeString(self, s: str) -> str:
        res = []
        freqs = defaultdict(int)

        for c in s:
            freqs[c] += 1

        max_heap = []
        for char, count in freqs.items():
            heappush(max_heap, (-count, char))
        
        while len(max_heap) >= 2:
            count1, c1 = heappop(max_heap)
            count2, c2 = heappop(max_heap)
            count1 += 1
            count2 += 1
            res.append(c1)
            res.append(c2)
            if count1 < 0: heappush(max_heap, (count1, c1))
            if count2 < 0: heappush(max_heap, (count2, c2))

        if max_heap:
            cnt, c = heappop(max_heap)
            cnt *= -1
            if cnt > 1: return ""
            res.append(c)
        return "".join(res)
                
            