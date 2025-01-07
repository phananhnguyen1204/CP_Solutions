class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        """
        0: red
        1: blue
        2: green


        dfs(i, red) = 1 + dfs(i - 1, blue) + 1 + dfs(i - 1, green)
        """

        memo = {}   
        n = len(costs)
        colors = [0, 1, 2]


        def dfs(i, color):
            if i < 0:
                return 0

            if (i, color) in memo:
                return memo[(i, color)]

            way = 0

            for color in colors: