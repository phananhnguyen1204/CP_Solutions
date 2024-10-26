class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        curr = []
        res = []
        n = len(nums)
        freq = {}
        for num in nums:
            if num not in freq:
                freq[num] = 1
            else:
                freq[num] += 1

        def dfs():
            if len(curr) == n:
                res.append(curr[:])
            for num in freq:
                if freq[num] > 0:
                    curr.append(num)
                    freq[num] -= 1
                    dfs()
                    freq[num] += 1
                    curr.pop()

        dfs()
        return res
