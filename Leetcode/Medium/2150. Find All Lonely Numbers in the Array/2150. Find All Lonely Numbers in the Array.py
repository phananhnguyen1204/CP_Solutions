class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
        seen = defaultdict(int)

        for num in nums:
            seen[num] += 1

        res = []
        for num in nums:
            if num + 1 not in seen and num - 1 not in seen and seen[num] == 1:
                res.append(num)

        return res