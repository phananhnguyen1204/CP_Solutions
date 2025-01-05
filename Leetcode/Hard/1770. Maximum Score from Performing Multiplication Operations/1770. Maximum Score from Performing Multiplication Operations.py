class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        n1, n2 = len(nums), len(multipliers)
        memo = {}
        
        def dfs(l, idx):
            if idx >= n2:
                return 0

            if (l, idx) in memo:
                return memo[(l, idx)]
                
            r = n1 - 1 - (idx - l)
            
            left = nums[l] * multipliers[idx] + dfs(l + 1, idx + 1)
            right = nums[r] * multipliers[idx] + dfs(l, idx + 1)

            memo[l, idx] = max(left, right)
            return memo[(l, idx)]

        return dfs(0, 0)