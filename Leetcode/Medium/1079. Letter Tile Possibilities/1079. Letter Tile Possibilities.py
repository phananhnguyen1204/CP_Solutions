class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        freq = defaultdict(int)

        for tile in tiles:
            freq[tile] += 1

        res = 0
        def backtrack():
            nonlocal res
            for c in freq:
                if freq[c] > 0:
                    res += 1
                    freq[c] -= 1
                    backtrack()
                    freq[c] += 1

        backtrack()
        return res