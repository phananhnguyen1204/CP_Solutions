class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        """
        queries[i][0] from 0 -> limit
        [0, 4, 5, 3, 4]

        ball_color = {
            1: 4,
            2: 5,
            3: 4

        }
        2 hashmap
        1 map keep track of freqs of colors
        1 map keep track of the color of each bal
        """

        balls = defaultdict(int)
        colors = defaultdict(int)
        res = []
        for ball, color in queries:
            if ball not in balls:
                balls[ball] = color
            else:
                old_color = balls[ball]
                if colors[old_color] == 1:
                    del colors[old_color]
                else:
                    colors[old_color] -= 1
                balls[ball] = color
            colors[color] += 1
            res.append(len(colors))
        return res
