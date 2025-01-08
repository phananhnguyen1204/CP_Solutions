class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        columns = defaultdict(set)
        for x, y in points:
            columns[x].add(y)

        n = len(points)
        min_area = float("inf")

        for i in range(n):
            for j in range(n):
                x1, y1 = points[i]
                x2, y2 = points[j]

                if x1 != x2 and y1 != y2:
                    if y2 in columns[x1] and y1 in columns[x2]:
                       min_area = min(min_area, abs(x1 - x2) * abs(y2 - y1))


        return min_area if min_area != float("inf") else 0