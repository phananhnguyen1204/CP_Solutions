class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        res = []
        cnt = {}
        for num in nums:
            row = cnt.get(num, 0)
            if len(res) == row:
                res.append([])
            cnt[num] = cnt.get(num, 0) + 1
            res[row].append(num)

        return res
        