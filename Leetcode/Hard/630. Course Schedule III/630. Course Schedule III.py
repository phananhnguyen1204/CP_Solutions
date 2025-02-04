from heapq import heappush, heappop
class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        """
        [[5,5],[4,6],[2,6]]
        """
        res = 0
        # if course have same deadline, -> prioritize taking the course with less duration

        courses.sort(key = lambda x : (x[1], x[0]))
        max_heap = []

        time = cnt = 0

        n = len(courses)
        for i in range(n):
            duration, lastDay = courses[i]
            heappush(max_heap, [-duration, lastDay])
            if time + duration > lastDay:
                if max_heap:
                    time -= -heappop(max_heap)[0]
                    cnt -= 1
            cnt += 1
            time += duration
            res = max(res, cnt)
        return res
        