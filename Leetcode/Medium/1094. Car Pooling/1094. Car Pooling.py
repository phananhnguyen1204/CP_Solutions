from heapq import heappush, heappop
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        timestamps = []

        for num, s, e in trips:
            timestamps.append([s, num])
            timestamps.append([e, -num])

        timestamps.sort()
        count = 0
        for i in range(len(timestamps)):
            count += timestamps[i][1]
            if count > capacity:
                return False
        
        return True
        

        