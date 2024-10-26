class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        used = [False] * n
        curr = []
        res = []
        def dfs(curr, used):
            if len(curr) == n:
                res.append(curr[:])
                print(res)
                return

            for i in range(n):
                if not used[i]:
                    used[i] = True
                    curr.append(nums[i])
                    dfs(curr, used)
                    curr.pop()
                    used[i] = False
                    

        dfs(curr, used)

        return res