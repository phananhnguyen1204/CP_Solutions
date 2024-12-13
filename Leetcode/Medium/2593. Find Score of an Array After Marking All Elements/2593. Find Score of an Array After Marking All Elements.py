from heapq import heappush
class Solution:
    def findScore(self, nums: List[int]) -> int:
        n = len(nums)
        mark = set()
        smallest_integer = []

        for i, num in enumerate(nums):
            heappush(smallest_integer, (num, i))

        score = 0

        while smallest_integer:
            curr, i = heappop(smallest_integer)

            if i not in mark:
                mark.add(i)

                score += curr
                if i > 0:
                    mark.add(i - 1)
                if i < n - 1:
                    mark.add(i + 1)

        return score
            