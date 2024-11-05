class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        
        def dfs(idx, curr, target):
            if target == 0:
                res.append(curr[:])
                return
            if target < 0: return
            for i in range(idx, len(candidates)):
                if i > idx and candidates[i] == candidates[i - 1]:
                    continue
                
                curr.append(candidates[i])
                dfs(i + 1, curr, target - candidates[i])
                curr.pop()

        dfs(0, [], target)
        return res