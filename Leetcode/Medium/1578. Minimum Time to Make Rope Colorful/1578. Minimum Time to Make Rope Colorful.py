class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        res = 0
        prev = 0
        for curr in range(1, len(colors)):
            if colors[curr] == colors[prev]:
                if neededTime[curr] >= neededTime[prev]:
                    res += neededTime[prev]
                    prev = curr
                else:
                    res += neededTime[curr]
            else:
                prev = curr
        return res