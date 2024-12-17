from heapq import heappush, heappop
class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        res = ""
        max_heap = []

        freq = {}
        for c in s:
            freq[c] = freq.get(c, 0) + 1
        
        for key, val in freq.items():
            heappush(max_heap, (-ord(key), val))

        while max_heap:
            c, cnt = heappop(max_heap)
            c *= -1
            c = chr(c)
            
            use = min(cnt, repeatLimit)
            res += use * c
            if cnt > use and max_heap:
                next_c, next_cnt = heappop(max_heap)
                next_c = chr(next_c * (-1))
                res += next_c

                if next_cnt > 1:
                    heappush(max_heap, (-ord(next_c), next_cnt - 1))
                heappush(max_heap, (-ord(c), cnt - use))
        
        return res
        