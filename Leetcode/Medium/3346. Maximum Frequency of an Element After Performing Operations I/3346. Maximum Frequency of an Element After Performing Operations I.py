class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        
        """
        [1, 4, 5]

        [0, 3, 4]
        """

        freq = defaultdict(int)
        points = set()
        points_cover = defaultdict(int)
        
        for num in nums:
            freq[num] += 1
            points_cover[num-k] += 1
            points_cover[num + k + 1] -= 1
            points.update({num, num - k, num + k + 1})
        
        points_cover_so_far = 0
        res = 0
        for point in sorted(points):
            points_cover_so_far += points_cover[point]
            res = max(res, freq[point] + min(points_cover_so_far - freq[point], numOperations))

        return res
        