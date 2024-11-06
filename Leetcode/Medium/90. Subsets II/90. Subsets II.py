class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(idx, curr):
            res.append(curr[:])
            for i in range(idx, len(nums)):
                if i > idx and nums[i] == nums[i - 1]: continue
                curr.append(nums[i])
                dfs(i + 1, curr)
                curr.pop()
        dfs(0, [])
        return res