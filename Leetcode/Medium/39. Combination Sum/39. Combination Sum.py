class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(target, curr, start):
            if target == 0:
                res.append(curr[:])
                return
            if target < 0:
                return
            
            for i in range(start, len(candidates)):
                curr.append(candidates[i])
                dfs(target - candidates[i], curr, i)
                curr.pop()
        dfs(target, [], 0)
        return res